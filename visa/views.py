# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ResidentCountry, TraditionalVisaR, EVisaR, VisaFreeR, CitizenshipCountry, TraditionalVisaC, EVisaC, VisaFreeC, CountryProduct, CountryForm, CountryFormResponse, userWishlist, Payment
from .serializers import TraditionalVisaSerializer, EVisaSerializer, VisaFreeSerializer, ResidentCountrySerializer, CitizenshipCountrySerializer, TraditionalVisaCSerializer, EVisaCSerializer, VisaFreeCSerializer, CountryProductSerializer, CountryFormSerializer, CountryFormResponseSerializer, userWishlistSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
import stripe
from django.conf import settings
from django.core.mail import send_mail


class CountryDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, country_name=None):
        if country_name:
            try:
                country = ResidentCountry.objects.get(name=country_name)
            except ResidentCountry.DoesNotExist:
                return Response({"error": "Country not found"}, status=404)

            country_serializer = ResidentCountrySerializer(country)

            traditional_visas = TraditionalVisaR.objects.filter(country=country)
            evisas = EVisaR.objects.filter(country=country)
            visa_free = VisaFreeR.objects.filter(country=country)

            traditional_visas_serializer = TraditionalVisaSerializer(traditional_visas, many=True)
            evisas_serializer = EVisaSerializer(evisas, many=True)
            visa_free_serializer = VisaFreeSerializer(visa_free, many=True)

            data = {
                'country': country_serializer.data,
                'traditional_visas': traditional_visas_serializer.data,
                'evisas': evisas_serializer.data,
                'visa_free': visa_free_serializer.data
            }
        else:
            countries = ResidentCountry.objects.all()
            countries_serializer = ResidentCountrySerializer(countries, many=True)

            data = {
                'countries': countries_serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

class CitizenshipCountryDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, country_name=None):
        if country_name:
            try:
                country = CitizenshipCountry.objects.get(name=country_name)
            except CitizenshipCountry.DoesNotExist:
                return Response({"error": "Country not found"}, status=404)

            country_serializer = CitizenshipCountrySerializer(country)

            traditional_visas = TraditionalVisaC.objects.filter(country=country)
            evisas = EVisaC.objects.filter(country=country)
            visa_free = VisaFreeC.objects.filter(country=country)

            traditional_visas_serializer = TraditionalVisaCSerializer(traditional_visas, many=True)
            evisas_serializer = EVisaCSerializer(evisas, many=True)
            visa_free_serializer = VisaFreeCSerializer(visa_free, many=True)

            data = {
                'country': country_serializer.data,
                'traditional_visas': traditional_visas_serializer.data,
                'evisas': evisas_serializer.data,
                'visa_free': visa_free_serializer.data
            }
        else:
            countries = CitizenshipCountry.objects.all()
            countries_serializer = CitizenshipCountrySerializer(countries, many=True)

            data = {
                'countries': countries_serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    

class CountryProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, country_name=None):
        if country_name:
            try:
                country = CountryProduct.objects.get(country_name=country_name)
            except CountryProduct.DoesNotExist:
                return Response({"error": "Country not found"}, status=404)

            country_serializer = CountryProductSerializer(country)

            forms = CountryForm.objects.filter(country=country).order_by('id')
            forms_serializer = CountryFormSerializer(forms, many=True)

            data = {
                'country': country_serializer.data,
                'forms': forms_serializer.data
            }
        else:
            countries = CountryProduct.objects.all()
            countries_serializer = CountryProductSerializer(countries, many=True)

            data = {
                'countries': countries_serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)



class CountryFormResponseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = CountryFormResponseSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            # Save the serializer and associate it with the user
            country_form_response = serializer.save(user=request.user)

            # Prepare email details
            user_name = request.user.full_name  # or request.user.username if you prefer
            country_name = data.get('country_name')  # Adjust this based on how you're sending the country in your data
            user_email = request.user.email  # Assuming the user model has an email field

            # Construct the email body with form data
            form_data_details = self.construct_form_data_details(serializer.data)

            # Send email notification
            send_mail(
                subject='Visa Application Form Submitted to Travel with Hydra',
                message=(
                    f"Dear {user_name},\n\n"
                    f"Thank you for submitting your visa application for {country_name} to Travel with Hydra. "
                    "You can track the status of your application from the profile page of your Travel with Hydra account.\n\n"
                    "Best Regards,\n"
                    "Travel with Hydra"
                ),
                from_email='info@travelwithydra.com',
                recipient_list=[user_email],
                fail_silently=False  # Set to True to suppress errors during sending
            )

            send_mail(
                subject='New Visa Application Form Received',
                message=(
                    f"Dear Admin,\n\n"
                    f"You have received a new visa application from {user_name} for {country_name}. "
                    "find the attached visa application form below:\n\n"
                    f"{form_data_details}\n\n"
                    "Best Regards,\n"
                    "Travel with Hydra"
                ),
                from_email='info@travelwithydra.com',
                recipient_list=['info@travelwithydra.com'],
                fail_silently=False  # Set to True to suppress errors during sending
            )


            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def construct_form_data_details(self, form_data):
        """Construct a string representation of the form data for the email body."""
        details = []
        for key, value in form_data.items():
            details.append(f"{key}: {value}")
        return "\n".join(details)



class MyApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        responses = CountryFormResponse.objects.filter(user=request.user).order_by('-id')
        serializer = CountryFormResponseSerializer(responses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def view_all_application_admin(request):
    applications = CountryFormResponse.objects.all().order_by('-id')
    formatted_applications = []

    for app in applications:
        responses = app.responses
        formatted_responses = {}
        if isinstance(responses, dict):
            for key, value in responses.items():
                formatted_responses[key] = value
        formatted_applications.append({
            'user': app.user,
            'country_name': app.country_name,
            'visa_type': app.visa_type,
            'status': app.status,
            'responses': formatted_responses
        })

    return render(request, 'view_all_application_admin.html', {'applications': formatted_applications})

class userWishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        country = request.data.get('country')
        
        if not country:
            return Response({"detail": "Country is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'user': request.user.id,
            'country': country
        }
        
        serializer = userWishlistSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        wishlists = userWishlist.objects.filter(user=request.user)
        serializer = userWishlistSerializer(wishlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Retrieve logged-in user's details
            user = request.user
            email = user.email
            full_name = user.full_name

            # Extract the UUID and price from the request payload
            payment_uuid = request.data.get('uuid')
            price = int(float(request.data.get('price')) * 100)  # Convert to cents

            if not payment_uuid:
                return Response({'error': 'UUID is required.'}, status=status.HTTP_400_BAD_REQUEST)

            customer = stripe.Customer.create(
                email=email,
                name=full_name
            )

            # Create the payment intent
            intent = stripe.PaymentIntent.create(
                amount=price,  # Amount in cents
                currency='gbp',
                payment_method_types=['card'],
                description='Travel with Hydra',
                metadata={
                    'payment_uuid': payment_uuid,
                    'user_id': str(user.id),
                },
                customer=customer.id,
            )

            # Save the payment record in the database
            Payment.objects.create(
                user=user,
                form_id=payment_uuid,
                amount=price / 100,  # Convert back to original amount
                status='Pending'  # Default status
            )

            # Return the client secret and intent ID for further use
            return Response({
                'client_secret': intent.client_secret,
                'intent_id': intent.id
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# serializers.py
from rest_framework import serializers
from .models import ResidentCountry, TraditionalVisaR, EVisaR, VisaFreeR, CitizenshipCountry, TraditionalVisaC, EVisaC, VisaFreeC, CountryProduct, CountryForm, CountryFormResponse, userWishlist, Payment
import os
from django.core.files.base import ContentFile
import base64
import io
from django.conf import settings


class ResidentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentCountry
        fields = ['name', 'flag']

class TraditionalVisaSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = TraditionalVisaR
        fields = ['destination_country']

class EVisaSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = EVisaR
        fields = ['destination_country']

class VisaFreeSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = VisaFreeR
        fields = ['destination_country']

class CitizenshipCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenshipCountry
        fields = ['name', 'flag']
    
class TraditionalVisaCSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = TraditionalVisaC
        fields = ['destination_country']

class EVisaCSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = EVisaC
        fields = ['destination_country']

class VisaFreeCSerializer(serializers.ModelSerializer):
    destination_country = serializers.CharField(source='get_destination_country_display')

    class Meta:
        model = VisaFreeC
        fields = ['destination_country']
    
class CountryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountryProduct
        fields = ['country_name', 'visa_type' , 'banner', 'description','description_rich', 'price_per_person', 'active']

class CountryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryForm
        fields = ['field_label', 'field_type', 'required']


class CountryFormResponseSerializer(serializers.ModelSerializer):
    files = serializers.DictField(
        child=serializers.CharField(),  # Expecting base64 strings
        write_only=True,
        required=False
    )

    class Meta:
        model = CountryFormResponse
        fields = ['id', 'application_date', 'user', 'country_name', 'visa_type', 'form_id', 'responses', 'status', 'files']

    def create(self, validated_data):
        files = validated_data.pop('files', {})
        responses = validated_data.get('responses', {})

        for field_label, base64_data in files.items():
            format, imgstr = base64_data.split(';base64,')  # Split data and format
            ext = format.split('/')[-1]  # Extract file extension
            file_data = ContentFile(base64.b64decode(imgstr), name=f"{field_label}.{ext}")

            user_folder = f"user_{self.context['request'].user.id}"
            upload_path = os.path.join('media', 'uploads', 'form_responses', user_folder)
            os.makedirs(upload_path, exist_ok=True)

            file_name = file_data.name
            file_path = os.path.join(upload_path, file_name)

            with open(file_path, 'wb+') as destination:
                for chunk in file_data.chunks():
                    destination.write(chunk)

            responses[field_label] = f"{settings.MEDIA_URL}uploads/form_responses/{user_folder}/{file_name}"

        # Create the instance and save the responses
        instance = CountryFormResponse.objects.create(**validated_data)
        instance.responses = responses
        instance.save()

        return instance


class userWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = userWishlist
        fields = ['user','country']
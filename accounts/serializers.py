
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)
    citizenship_country = serializers.CharField(required=True)
    resident_country = serializers.CharField(required=True)

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.full_name = self.data.get('full_name', '')
        user.mobile_number = self.data.get('mobile_number', '')
        user.citizenship_country = self.data.get('citizenship_country', '')
        user.resident_country = self.data.get('resident_country', '')
        user.save()
        return user
    
class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('full_name', 'mobile_number', 'citizenship_country', 'resident_country')


User = get_user_model()

class CustomPasswordResetSerializer(PasswordResetSerializer):
    def validate_email(self, value):
        # Get the user based on email
        email = value
        self.user = User.objects.filter(email=email).first()

        if not self.user:
            raise serializers.ValidationError("A user with that email was not found.")

        return value

    def get_email_options(self):
        request = self.context.get('request')
        current_site = get_current_site(request)

        # Create the password reset URL
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_url = f"https://travelwithydra.com/newpassword?uid={uid}&token={token}"

        # Custom email content
        subject = "Password Reset Request"
        email_body = f"""
        Dear {self.user.full_name},

        We received a request to reset your password for your Travel With Hydra account. To proceed, please click the link below to set a new password:

        {reset_url}

        If you did not request this change, please ignore this email or contact support for assistance.

        Regards,
        Travel With Hydra
        """
        
        return {
            'subject': subject,
            'body': email_body,
            'to': [self.user.email],
        }
    
    def save(self):
        email_options = self.get_email_options()
        send_mail(
            email_options['subject'],
            email_options['body'],
            None,  # Use default from_email
            email_options['to']
        )


from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomPasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password1 = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        uid = attrs.get('uid')
        token = attrs.get('token')
        new_password1 = attrs.get('new_password1')
        new_password2 = attrs.get('new_password2')

        # Validate that both password fields match
        if new_password1 != new_password2:
            raise ValidationError("The two password fields must match.")

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError("Invalid UID or user does not exist.")

        if not default_token_generator.check_token(user, token):
            raise ValidationError("Invalid or expired token.")

        attrs['user'] = user
        attrs['new_password'] = new_password1
        return attrs

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()

from rest_framework import serializers
from .models import Header, Hero, customerStories, Footer, FAQSection, FAQ, ContactForm, Blog
from django.conf import settings

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class customerStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerStories
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class FAQSectionSerializer(serializers.ModelSerializer):
    faqs = FAQSerializer(many=True, read_only=True)

    class Meta:
        model = FAQSection
        fields = ['id', 'banner_image', 'faqs']


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        fields = ['id', 'title', 'category', 'image', 'excerpt', 'content', 'content_rich']

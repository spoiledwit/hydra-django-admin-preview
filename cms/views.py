from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Header, Hero, customerStories, Footer, FAQSection, ContactForm, Blog
from .serializers import HeaderSerializer, HeroSerializer, customerStoriesSerializer, FooterSerializer, FAQSectionSerializer, ContactFormSerializer, BlogSerializer

class HeaderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        header = Header.objects.first()
        if header:
            serializer = HeaderSerializer(header)
            return Response(serializer.data)
        return Response({"detail": "Header not found."}, status=status.HTTP_404_NOT_FOUND)


class HeroView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        hero = Hero.objects.first()
        if hero:
            serializer = HeroSerializer(hero)
            return Response(serializer.data)
        return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)


class customerStoriesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        customer_stories = customerStories.objects.all()
        if customer_stories.exists():
            serializer = customerStoriesSerializer(customer_stories, many=True)
            return Response(serializer.data)
        return Response({"detail": "No customer stories found."}, status=status.HTTP_404_NOT_FOUND)


class FooterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        footer = Footer.objects.first()
        if footer:
            serializer = FooterSerializer(footer)
            return Response(serializer.data)
        return Response({"detail": "Footer not found."}, status=status.HTTP_404_NOT_FOUND)


class FAQSectionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        sections = FAQSection.objects.all()
        if sections.exists():
            serializer = FAQSectionSerializer(sections, many=True)
            return Response(serializer.data)
        return Response({"detail": "No FAQ sections found."}, status=status.HTTP_404_NOT_FOUND)


class ContactFormView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category=None, format=None):
        if category:
            # Filter blogs by the category slug from the URL
            blogs = Blog.objects.filter(category=category)
        else:
            # Return all blogs if no category is provided
            blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data)


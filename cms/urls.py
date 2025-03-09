from django.urls import path
from .views import HeaderView, HeroView, customerStoriesView, FooterView, FAQSectionView, ContactFormView, BlogListView, BlogDetailView

urlpatterns = [
    path('header/', HeaderView.as_view(), name='header'),
    path('hero/', HeroView.as_view(), name='hero'),
    path('customer-stories/', customerStoriesView.as_view(), name='customer-stories'),
    path('footer/', FooterView.as_view(), name='footer'),
    path('faqs/', FAQSectionView.as_view(), name='faqs'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<str:category>', BlogListView.as_view(), name='blog-list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

]

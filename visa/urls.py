# urls.py
from django.urls import path
from .views import CountryDetailView, CitizenshipCountryDetailView, CountryProductListView, CountryFormResponseView, MyApplicationsView, view_all_application_admin, userWishlistView, CreatePaymentIntentView

urlpatterns = [
    path('resident-country/<str:country_name>/', CountryDetailView.as_view(), name='country-detail'),
    path('citizenship-country/<str:country_name>/', CitizenshipCountryDetailView.as_view(), name='citizenship-country-detail'),
    path('resident-country/', CountryDetailView.as_view(), name='country-detail'),
    path('citizenship-country/', CitizenshipCountryDetailView.as_view(), name='citizenship-country-detail'),
    path('country/', CountryProductListView.as_view(), name='country-product-detail'),
    path('country/<str:country_name>/', CountryProductListView.as_view(), name='country-product-detail'),
    path('submit-application-form/', CountryFormResponseView.as_view(), name='submit-application-form'),
    path('my-applications/', MyApplicationsView.as_view(), name='application'),
    path('all-applications/', view_all_application_admin, name='all-applications'),
    path('wishlist/', userWishlistView.as_view(), name='wishlist'),
    path('create-payment-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),

]

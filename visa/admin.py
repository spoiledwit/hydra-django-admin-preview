from django.contrib import admin
from .models import ResidentCountry, TraditionalVisaR, EVisaR, VisaFreeR, CitizenshipCountry, TraditionalVisaC, EVisaC, VisaFreeC, CountryProduct, CountryForm, CountryFormResponse, userWishlist, Payment
from django.urls import reverse
from django.utils.html import format_html
class TraditionalVisaInline(admin.TabularInline):  # or admin.StackedInline
    model = TraditionalVisaR
    extra = 1

class EVisaInline(admin.TabularInline):  # or admin.StackedInline
    model = EVisaR
    extra = 1

class VisaFreeInline(admin.TabularInline):  # or admin.StackedInline
    model = VisaFreeR
    extra = 1


class ResidentCountryAdmin(admin.ModelAdmin):
    list_per_page = 10000
    inlines = [TraditionalVisaInline, EVisaInline, VisaFreeInline]

admin.site.register(ResidentCountry, ResidentCountryAdmin)

class TraditionalVisaCInline(admin.TabularInline):  # or admin.StackedInline
    model = TraditionalVisaC
    extra = 1

class EVisaCInline(admin.TabularInline):  # or admin.StackedInline
    model = EVisaC
    extra = 1

class VisaFreeCInline(admin.TabularInline):  # or admin.StackedInline
    model = VisaFreeC
    extra = 1

class CitizenshipCountryAdmin(admin.ModelAdmin):
    list_per_page = 10000
    inlines = [TraditionalVisaCInline, EVisaCInline, VisaFreeCInline]

admin.site.register(CitizenshipCountry, CitizenshipCountryAdmin)

class CountryFormAdmin(admin.TabularInline):
    model = CountryForm
    extra = 1

class CountryProductAdmin(admin.ModelAdmin):
    list_per_page = 10000
    inlines = [CountryFormAdmin]

admin.site.register(CountryProduct, CountryProductAdmin)
    
class CountryFormResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'country_name', 'visa_type', 'status','form_id', 'view_link']
    search_fields = ['form_id']
    list_filter = ['user', 'visa_type', 'status']

    def view_link(self, obj):
        # Create a link to the detail view of the object
        url = '/api/visa/all-applications/'
        return format_html('<a href="{}">View</a>', url)

    view_link.short_description = 'View'
admin.site.register(CountryFormResponse, CountryFormResponseAdmin)


class userWishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'country']
    list_filter = ['user', 'country']

admin.site.register(userWishlist, userWishlistAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'form_id', 'amount', 'status']
    search_fields = ['form_id']
    list_filter = ['user', 'status']

admin.site.register(Payment, PaymentAdmin)

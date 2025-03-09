from django.contrib import admin
from .models import Header, Hero, customerStories, Footer, FAQSection, FAQ, ContactForm, Blog


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    pass

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass

@admin.register(customerStories)
class customerStoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

class FAQSectionAdmin(admin.ModelAdmin):
    inlines = [FAQInline]


admin.site.register(FAQSection, FAQSectionAdmin)
admin.site.register(Blog)

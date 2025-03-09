from django.db import models
from accounts.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field


COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cabo Verde', 'Cabo Verde'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'),
        ('Congo, Republic of the', 'Congo, Republic of the'),
        ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Eswatini', 'Eswatini'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, North', 'Korea, North'),
        ('Korea, South', 'Korea, South'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('North Macedonia', 'North Macedonia'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestine', 'Palestine'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Sudan, South', 'Sudan, South'),
        ('Suriname', 'Suriname'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Timor-Leste', 'Timor-Leste'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]

class ResidentCountry(models.Model):
    name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    flag = models.ImageField(upload_to='images/flags/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resident Countries"

    def __str__(self):
        return self.name


class TraditionalVisaR(models.Model):
    country = models.ForeignKey(ResidentCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "Traditional Visa"

    def __str__(self):
        return f"{self.country.name}"
    

class EVisaR(models.Model):
    country = models.ForeignKey(ResidentCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "E Visa"
    
    def __str__(self):
        return f"{self.country.name}"


class VisaFreeR(models.Model):
    country = models.ForeignKey(ResidentCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "Visa Free"
    
    def __str__(self):
        return f"{self.country.name}"
    

######### CITIZENSHIP COUNTRIES #########

class CitizenshipCountry(models.Model):
    name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    flag = models.ImageField(upload_to='images/flags/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Citizenship Countries"

    def __str__(self):
        return self.name


class TraditionalVisaC(models.Model):
    country = models.ForeignKey(CitizenshipCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "Traditional Visa"

    def __str__(self):
        return f"{self.country.name}"
    

class EVisaC(models.Model):
    country = models.ForeignKey(CitizenshipCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "E Visa"
    
    def __str__(self):
        return f"{self.country.name}"


class VisaFreeC(models.Model):
    country = models.ForeignKey(CitizenshipCountry, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    

    class Meta:
        verbose_name_plural = "Visa Free"
    
    def __str__(self):
        return f"{self.country.name}"


visa_type = [
    ('traditional', 'Traditional'),
    ('e_visa', 'E Visa'),
    ('visa_free', 'Visa Free'), 
]

class CountryProduct(models.Model):
    country_name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    visa_type = models.CharField(max_length=100, choices=visa_type)
    banner = models.ImageField(upload_to='images/banners/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_rich = CKEditor5Field('Text' ,config_name='extends', blank=True, null=True)
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Country Products"

    def __str__(self):
        return f"{self.country_name}"

field_type_choices = [
    ('text', 'Text'),
    ('number', 'Number'),
    ('date', 'Date'),
    ('textarea', 'Textarea'),
    ('upload', 'Upload'),
]
class CountryForm(models.Model):
    country = models.ForeignKey(CountryProduct, on_delete=models.CASCADE)
    field_label = models.CharField(max_length=500)
    field_type = models.CharField(max_length=100, choices=field_type_choices)
    required = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Product Forms"
    
    def __str__(self):
        return f"{self.country.country_name}"
    

####### DYNAMIC FORM RESPONSES #######

application_status = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('With Embassy', 'With Embassy')
]

payment_status = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
    ('Failed', 'Failed'),
]

class CountryFormResponse(models.Model):
    form_id = models.CharField(max_length=100, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    application_date = models.DateTimeField(auto_now_add=True)
    visa_type = models.CharField(max_length=100, choices=visa_type)
    responses = models.JSONField(default=dict)
    status = models.CharField(max_length=50, default='Pending', choices=application_status)

    class Meta:
        verbose_name_plural = "Visa Applications"

    def __str__(self):
        return f"{self.user.username}"


class userWishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)

    class Meta:
        verbose_name_plural = "User Wishlist"

    def __str__(self):
        return f"{self.user.username}"
    

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    form_id = models.CharField(max_length=100, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='Pending', choices=payment_status)

    class Meta:
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.user.username}"
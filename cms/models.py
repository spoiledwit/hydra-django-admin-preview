from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Header(models.Model):
    logo = models.ImageField(upload_to='images/')
    menu_item_1 = models.CharField(max_length=100, blank=True, null=True)
    menu_item_1_link = models.CharField(max_length=100, blank=True, null=True)
    menu_item_2 = models.CharField(max_length=100, blank=True, null=True)
    menu_item_2_link = models.CharField(max_length=100, blank=True, null=True)
    menu_item_3 = models.CharField(max_length=100, blank=True, null=True)
    menu_item_3_link = models.CharField(max_length=100, blank=True, null=True)
    menu_item_4 = models.CharField(max_length=100, blank=True, null=True)
    menu_item_4_link = models.CharField(max_length=100, blank=True, null=True)
    menu_item_5 = models.CharField(max_length=100, blank=True, null=True)
    menu_item_5_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Header'
    
    class Meta:
        verbose_name_plural = 'Header'
    

class Hero(models.Model):
    hero_title = models.CharField(max_length=100, blank=True, null=True)
    hero_description = models.TextField(blank=True, null=True)
    hero_button_text = models.CharField(max_length=100, blank=True, null=True)
    hero_button_link = models.CharField(max_length=100, blank=True, null=True)
    hero_banner_image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    hero_banner_image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    hero_banner_image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    hero_banner_image4 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return 'Hero'

    class Meta:
        verbose_name_plural = 'Hero'



class customerStories(models.Model):
    testimonial_video = models.FileField(upload_to='videos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return 'Customer Stories'

    class Meta:
        verbose_name_plural = 'Customer Stories'


class Footer(models.Model):
    footer_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    footer_text_bottom = models.TextField(blank=True, null=True)
    footer_email = models.CharField(max_length=100, blank=True, null=True)
    footer_phone = models.CharField(max_length=100, blank=True, null=True)
    social_link_facebook = models.CharField(max_length=100, blank=True, null=True)
    social_link_twitter = models.CharField(max_length=100, blank=True, null=True)
    social_link_instagram = models.CharField(max_length=100, blank=True, null=True)
    social_link_linkedin = models.CharField(max_length=100, blank=True, null=True)
    social_link_youtube = models.CharField(max_length=100, blank=True, null=True)
    social_link_whatsapp = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return 'Footer'

    class Meta:
        verbose_name_plural = 'Footer'


class FAQSection(models.Model):
    banner_image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return "FAQ Section"

class FAQ(models.Model):
    section = models.ForeignKey(FAQSection, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Contact Form'


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

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    image = models.ImageField(upload_to='blog_images/')
    excerpt = models.TextField()
    content = models.TextField()
    content_rich = CKEditor5Field('Text' ,config_name='extends', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Blogs'

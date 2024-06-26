from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Member(models.Model):
  startup_name = models.CharField(max_length=300)
  starting_date = models.DateField()
  address = models.CharField(max_length=500)

  industry_name = (
        (1, "ITES"),
        (2, "Health Tech"),
        (3, "AI"),
        (4, "Ed Tech"),
        (5, "Logistics"),
        (6, "IOT"),
        (7, "Food Tech"),
        (8, "Renewable Energy"),
    )
  industry = models.IntegerField(choices=industry_name)
  
  product_description = models.TextField()

  stage_name = (
        (1, "Pre-Seed"),
        (2, "Seed"),
        (3, "Series A"),
        (4, "Series B"),
        (5, "Series C"),
    )
  stage = models.IntegerField(choices=stage_name)

  numbers_of_founders = models.IntegerField()
  team_size = models.IntegerField()
  investment_requirement = models.IntegerField()
  monthly_revenue = models.IntegerField()
  name = models.CharField(max_length=255)
  designation = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  linkedin = models.CharField(max_length=100, blank=True, null=True)
  website = models.CharField(max_length=100, blank=True, null=True)
  additional_documents = models.FileField(upload_to='document', blank=True, null=True)


  def __str__(self):
    return str(self.startup_name)
  

class Investor(models.Model):
  name = models.CharField(max_length=255)
  organigation = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  message = models.TextField()


  def __str__(self):
    return str(self.name)




class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    short_description = models.TextField(max_length=500)
    blog_content = RichTextField()
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)
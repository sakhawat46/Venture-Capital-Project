from django.db import models

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
  
  product_description = models.CharField(max_length=1000)

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
  designation = models.CharField(max_length=255)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  linkedin = models.CharField(max_length=100)
  website = models.CharField(max_length=100)
  additional_documents = models.FileField(upload_to='document')
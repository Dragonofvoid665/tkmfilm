from django.db import models

#
# class Actors(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     date_of_death = models.DateField(null=False, blank=True)
#     image = models.ImageField(upload_to="static/photos/", null=False, blank=False)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Rez(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     date_of_death = models.DateField(null=False, blank=True)
#     image = models.ImageField(upload_to="static/photos/", null=False, blank=False)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name

class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    companies = models.ManyToManyField(Company, related_name='products')

    def __str__(self):
        return self.name
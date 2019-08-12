from django.db import models

# Create your models here.
status_choice = (
        (None,"Please select below option"),
        ('1', 'Active'),
        ('2', 'inactive'),
        ('3', 'pending'),
    )

class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choice)


class Country(Base):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name


class Language(Base):
    name = models.CharField("lanuage name it is",max_length=100)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE, db_column='country_id')
    logo = models.ImageField(upload_to='logo')


    def __str__(self):
        return self.name


class Channels(Base):
    name = models.CharField(max_length=100)
    path = models.TextField(default=False)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, db_column='language_id')
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name





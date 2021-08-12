from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


class User(AbstractUser):
    pass


class ExampleModel(models.Model):
    # used for referring to other models in the database (i.e. the user that created the model)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='example_models')
    # used for integers
    ex_int_field = models.IntegerField()
    # used for strings
    ex_char_field = models.CharField(max_length=64)
    # used for long text
    ex_text_field = models.TextField()
    # used for dates (using auto_now_add=True means it is automatically created upon creation of an instance)
    ex_date_field = models.DateTimeField(auto_now_add=True)
    # used for booleans
    ex_bool_field = models.BooleanField()
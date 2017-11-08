from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class FormField(models.Model):
    fieldName = models.CharField(max_length=50)
    text = 'text'
    email = validate_email
    phone = PhoneNumberField()
    date = models.DateTimeField
    TYPE_OF_FIELD_CHOICE = (
        (text, 'text'),
        (email, 'example@email.mail'),
        (phone, '9123456789'),
        (date, '2017-01-01')
    )
    field_type = models.CharField(max_length=25,
                                   choices=TYPE_OF_FIELD_CHOICE,
                                   default=text)



    def __str__(self):
        return self.fieldName



class FormPattern(models.Model):
    formName = models.CharField(max_length=50)
    formFields = models.ManyToManyField(FormField)

    def __str__(self):
        return self.formName



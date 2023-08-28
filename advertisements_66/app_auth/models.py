from django.db import models

class User(models.Model):
    username = models.TextField('ник')
    name = models.TextField('имя')
    surname = models.TextField('фамилия')
    password1 = models.TextField('пароль')
    password2 = models.TextField('подтверждение пароля')
# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    promotion = models.BooleanField(default=False)


class Article (models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    update_at = models.DateTimeField(default=timezone.now)


class Departement (models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class Prix (models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    icone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class CustomUser(User):
    first_login = models.DateTimeField()


class Apropos(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class Autre(models.Model):
    grand_titre = models.CharField(max_length=100)
    petit_titre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20)
    pourquoi = models.TextField(blank=True)
    couverture = models.ImageField(upload_to='Couverture/', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


class Agence(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='Agence/', blank=True, null=True)
    is_active = models.BooleanField(default=True)


class Equipe(models.Model):
    photo = models.ImageField(upload_to='Equipe/', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)





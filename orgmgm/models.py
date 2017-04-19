from django.db import models


class Bundesland(models.Model):
    bundesland = models.CharField(max_length=25, verbose_name='Bundesland')

    def __str__(self):
        return self.bundesland

class Organisation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Organisation Name')
    strassehsnr = models.CharField(max_length=200, verbose_name='Strasse und Hausnummer')
    plz = models.CharField(max_length=5, verbose_name='Postleitzahl')
    stadt = models.CharField(max_length=50, verbose_name='Stadt')
    telefon = models.CharField(max_length=20, verbose_name='Telefonnummer')
    email = models.CharField(max_length=50, verbose_name='Email Adresse')
    www = models.CharField(max_length=100, verbose_name='Homepage')
    bundesland = models.ForeignKey(Bundesland)

    def __str__(self):
        return self.name

class Kontakt(models.Model):
    vorname = models.CharField(max_length=20, verbose_name='Vorname')
    nachname = models.CharField(max_length=20, verbose_name='Nachname')
    email = models.CharField(max_length=20, verbose_name='Email Adresse')
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nachname


class ActivityType(models.Model):
    activitytype = models.CharField(max_length=20, verbose_name='Activity Type')
    editdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.activitytype


class Activity(models.Model):
    titel = models.CharField(max_length=50, verbose_name='Title der Aktivität')
    activitydate = models.DateTimeField(verbose_name='Datum der Aktivität')
    description = models.CharField(max_length=200, verbose_name='Beschreibung')
    activitytype = models.ForeignKey(ActivityType, verbose_name='Art der Aktivität')
    organisation = models.ForeignKey(Organisation, verbose_name='Organisation')
    kontakt = models.ForeignKey(Kontakt, verbose_name='Kontakt')
    editdate = models.DateTimeField(auto_now_add=True, blank=True)
    #edituser = models.ForeignKey(Users) #check where user table from login stores

    def __str__(self):
        return self.title

# class Activity(models.self):
#     title
#     activitytype
#     date 
#     description
#     successrating
#     nextsteps
#     organisation
#     Kontakt
#     editdate
#     edituser





# Create your models here.

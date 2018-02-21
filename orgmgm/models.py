from django.db import models


class Bundesland(models.Model):
    bundesland = models.CharField(max_length=25, verbose_name='Bundesland')
    bundeslandshort = models.CharField(
        max_length=25, verbose_name='Bundesland Short')

    def __str__(self):
        return self.bundesland


class OrganisationType(models.Model):
    organisationtype = models.CharField(
        max_length=20, verbose_name='Organisation Type')
    editdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.organisationtype


class Organisation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Organisation Name')
    strassehsnr = models.CharField(
        max_length=200, verbose_name='Strasse und Hausnummer')
    plz = models.CharField(max_length=20, verbose_name='Postleitzahl')
    stadt = models.CharField(max_length=100, verbose_name='Stadt')
    telefon = models.CharField(max_length=50, verbose_name='Telefonnummer')
    email = models.CharField(max_length=100, verbose_name='Email Adresse')
    www = models.CharField(max_length=100, verbose_name='Homepage')
    bundesland = models.ForeignKey(Bundesland)
    organisationtype = models.ForeignKey(OrganisationType)

    def __str__(self):
        return self.name


class Kontakt(models.Model):
    ANREDE_OPT = ((1, 'Frau'), (2, 'Herr'), (3, 'Sonstige'))
    vorname = models.CharField(max_length=100, verbose_name='Vorname', null=True, blank=True)
    nachname = models.CharField(max_length=100, verbose_name='Nachname')
    anrede = models.IntegerField(choices=ANREDE_OPT, null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name='Email Adresse', null=True, blank=True)
    rolle = models.CharField(max_length=100, verbose_name='Rolle', null=True, blank=True)
    organisation = models.ForeignKey(Organisation)
    telefon = models.CharField(max_length=100, verbose_name='Telfonnummer', null=True, blank=True)

    def __str__(self):
        return self.nachname


class ActivityType(models.Model):
    activitytype = models.CharField(
        max_length=20, verbose_name='Activity Type')
    editdate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.activitytype


class Activity(models.Model):
    activitydate = models.DateField(verbose_name='Datum der Aktivität', null=True, blank=True)
    description = models.TextField(verbose_name='Beschreibung')
    activitytype = models.ForeignKey(
        ActivityType, verbose_name='Art der Aktivität', null=True, blank=True)
    organisation = models.ForeignKey(Organisation, verbose_name='Organisation')
    kontakt = models.ForeignKey(Kontakt, verbose_name='Kontakt', null=True, blank=True)
    editdate = models.DateField(auto_now=True, null=True, blank=True)
    # edituser = models.ForeignKey(Users)
    # check where user table from login stores

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name='Frage')
    answer = models.TextField()

    def __str__(self):
        return self.question

class Resource(models.Model):
    title = models.CharField(max_length=100, verbose_name='Resource Titel')
    link = models.URLField(verbose_name='Link')
    linktitle = models.CharField(max_length=100, verbose_name='Link Titel')
    description = models.TextField()

    def __str__(self):
        return self.title


from django.db import models


class Picture(models.Model):
    source = models.ImageField(null=True, default=None)
    processed = models.ImageField(null=True, default=None)
    id = models.AutoField(primary_key=True)


class Test(models.Model):
    source1 = models.IntegerField(blank=True, null=True)
    source2 = models.IntegerField(blank=True, null=True)
    source3 = models.IntegerField(blank=True, null=True)
    source4 = models.IntegerField(blank=True, null=True)
    source5 = models.IntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)


class Github(models.Model):
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
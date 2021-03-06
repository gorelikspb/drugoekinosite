from django.db import models
from django.template.defaultfilters import slugify

class Director(models.Model):
    name = models.CharField(max_length=120)
    image = models.CharField(max_length=400, default = '', blank = True)
    kp_id = models.PositiveIntegerField(null = True, blank = True)
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=150, blank = True)
    title_en = models.CharField(max_length=150, blank=True)
    image = models.CharField(max_length=400, default = '', blank = True)
    director = models.ForeignKey('Director',on_delete=models.PROTECT, null = True, blank = True, )
    year = models.PositiveIntegerField(null = True, blank = True)
    runtime = rating = models.PositiveSmallIntegerField(null = True, blank = True)
    videovk = models.CharField(max_length=400, null = True, blank = True)
    material = models.TextField(blank=True)
    kp_id = models.PositiveIntegerField(unique = True, null = True, blank = True)
    budget = models.PositiveIntegerField(null=True, blank=True)
    rating = models.FloatField(null = True, blank = True)
    votes = models.PositiveIntegerField(null = True, blank = True)
    imdb_rating = models.FloatField(null = True, blank = True)
    imdb_votes = models.PositiveIntegerField(null=True, blank=True)
    # stars = models.ManyToManyField('Actor',  null = True, blank = True,)
    kp_plot = models.TextField(blank = True)
    def __str__(self):
        return self.title
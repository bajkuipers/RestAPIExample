from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=100)
  release_date = models.DateField()
  original_language = models.CharField(max_length=5)
  last_update = models.DateTimeField(auto_now_add=True, null=True)

class Keyword(models.Model):
  name = models.CharField(max_length=100)
  movie = models.ForeignKey(Movie, related_name='keywords')
  last_update = models.DateTimeField(auto_now_add=True, null=True)

class Crew(models.Model):
  name = models.CharField(max_length=100)
  job = models.CharField(max_length=100)
  movie = models.ForeignKey(Movie, related_name='crew')
  last_update = models.DateTimeField(auto_now_add=True, null=True)

class Cast(models.Model):
  name = models.CharField(max_length=100)
  character = models.CharField(max_length=100)
  movie = models.ForeignKey(Movie, related_name='cast')
  last_update = models.DateTimeField(auto_now_add=True, null=True)

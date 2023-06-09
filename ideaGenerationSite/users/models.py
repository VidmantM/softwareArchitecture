from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import sys
sys.path.append("..")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill', blank=True)
    interests = models.ManyToManyField('Interest', blank=True)
    projects = models.ManyToManyField('Project', blank=True)
    liked_projects = models.ManyToManyField('Project', related_name='users_liked', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Skill(models.Model):
    # ID - Django by default creates it and assigns it as PK
    name = models.CharField(max_length=30, unique=False, verbose_name="Name of subject", default="name")     # Python, Django, etc
    expertise = models.CharField(max_length=30, unique=False, verbose_name="Skill level", default="Intermediate")     # Beginner, Intermediate, Skilled

    def __str__(self):
        return f'{self.name, self.expertise}'


class Interest(models.Model):
    # ID - Django by default creates it and assigns it as PK
    name = models.CharField(max_length=30, unique=False, verbose_name="Name of subject", default="name")     # Python, Django, etc
    expertise = models.CharField(max_length=30, unique=False, verbose_name="Skill level", default="Intermediate")     # Beginner, Intermediate, Skilled

    def __str__(self):
        return f'{self.name, self.expertise}'

class Weight(models.Model):
    # ID - Django by default creates it and assigns it as PK
    purpose = models.CharField(max_length=30, unique=False, verbose_name="Name of the formula", default="name")
    formula = models.CharField(max_length=100, unique=False, verbose_name="Mathematical weight formula", default="1")

    def __str__(self):
        return f'{self.purpose}'

class Project(models.Model):
    # ID - Django by default creates it and assigns it as PK

    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')
    skills = models.ManyToManyField('Skill')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)  # New field for project approval

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

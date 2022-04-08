from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField()

    def __str__(self):
        return self.name

class Skills(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=50)

class SocialMedia(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='social_media')
    social_media = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

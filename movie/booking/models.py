from django.db import models

# Create your models here.

class moviebook(models.Model):
    movie_choices=[
        ('Sholey','Sholey 1975'),
        ('Avengers','Avengers end game'),
        ('Harry Potter','Harry potter and prizoner of Azkaban')

    ]
    ticket_choices = [
        ('gold',300),
        ('silver',150)
    ]
    name=models.CharField(max_length=200)
    movie=models.CharField(max_length=200,choices=movie_choices)
    ticket=models.IntegerField(choices=ticket_choices),
    quantity=models.IntegerField()
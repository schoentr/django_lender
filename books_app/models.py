from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.IntegerField()
    date_added = models.DateField(default=timezone.now)
    last_borrowed = models.DateTimeField(blank=True,auto_now=True)

    STATES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-Out'),
    ]
    
    status = models.CharField(choices=STATES, default='available', max_length=48)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'
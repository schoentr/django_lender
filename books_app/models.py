from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.IntegerField(4)
    # date_added =
    # last_borrowed = 




    STATES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-Out'),
    ]
    status = models.CharField(choices=STATES, default='available', max_length=48)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'
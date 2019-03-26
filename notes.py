# python manange.py startapp notes_app   --> in terminal


# in models.py

from django.db import models
# create your models here.

Class Note(models.Model):
    """doc string"""

    title=models.CharField(max_length=48)
    detail=models.CharField(max_length=4096)

    STATES=[
        ('incomplete','Incomplete'),
        ('complete','Complete'),
    ]


    status = models.CharField(choices=STATES, default='incomplete', max_length=48)

    added = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateField(auto_now=True)
   
    def __repr__(self):
        return f'<Note: {self.title} | Status: {self.status}>'
    
    def __str__(self):
        return f'<Note: {self.title} | Status: {self.status}>'


## IN ADMIN PANEL

from .models import Note

# registre
admin.site.register(Note)

## IN SETTINGS
--> add to installed apps

##  Need to make migrations



## Docker Commands
--> docker ps -a     $shows all containers
--> docker exec -it   <<container name>>    $opens an interactive termaial viewing container
--> docker-compose up build 
--> docker-compose down    $ shuts down the container
--> docker volume ls   $ shows all the volumes
--> docker volume rm <volume name>  $ removes volume
## inside container  to create admin
--> python manage.py createsuperuser  




###  creating a view

from django.shortchts import render, get_list_or_404, get_object_or_404
from .models import Note

## create your views here

def note_list_views(request):

    notes = get_list_or_404
    context= {
        'notes':notes
    }
    return render(request,'notes/note_list.html', context)

def note_detail_view(request, pk=None):
    note = get_object_or_404(Note,id=pk)
    context{
        'note': note
    }
    return render(request,'notes/note_detail.html',)

## create urls.py in app

from django.urls import path
from .views import note_detail_view, note_list_views

urlpatterns = [
    path('',note_list_view, name='note_detail'),
    path('<int:pk>',note_detail_view, name='note-detail'),
    
]
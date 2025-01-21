from django.db import models
#a model tells Django how to work with the data that will be stored in the app
#a model is like a class
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about"""
    #the topic class inherits from Model, a parent class that defines the functionality of a Model
    text = models.CharField(max_length=200) #storing small amounts of text using 'CharField'
    date_added = models.DateTimeField(auto_now_add=True) #recording date and time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the Model"""
        return self.text #displaying a simple representation of a model

class Entry(models.Model):
    """Something specific learning about a topic"""
    #a foreign key is a database term, it's a reference to another record in the database
    #matching each entry to a specific topic
    #on_delete=models.CASCADE means that when a topic is deleted, all the entries associated with that topic are deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #text is an instance of TextField
    text = models.TextField()
    #recording the date added
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #meta holds extra information for managing a model, it allows us to set a special attribute telling Django to use 'Entries'
        #when it needs to refer to more than one entry
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        #which information to be shown when it refers to individual entries
        return self.text[:50] + "..."



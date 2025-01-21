from rest_framework import serializers
from .models import Topic, Entry

class TopicSerializer(serializers.ModelSerializer):
    #converting 'Topic' objects into JSON
    class Meta:
        model = Topic
        fields = ['id', 'text']

class EntrySerializer(serializers.ModelSerializer):
    #converting 'Entry' objects to JSON
    class Meta:
        model = Entry
        fields = ['id', 'topic', 'text', 'date_added']

#these serializer are used to handle conversion between Python objects and JSON for the API

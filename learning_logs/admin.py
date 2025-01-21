from django.contrib import admin

from learning_logs.models import Topic, Entry  # importing the model we want to register, 'Topic'

admin.site.register(Topic) #telling Django to manage out model through the admin site
admin.site.register(Entry)


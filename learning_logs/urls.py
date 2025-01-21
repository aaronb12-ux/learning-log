"""Defines URL patterns for learning_logs"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, EntryViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'entries', EntryViewSet)

app_name = 'learning_logs'
urlpatterns = [
    path('api/', include(router.urls)), #route to API
    path('', views.index, name='index'), #route to main page 'index'
    path('topics/', views.topics, name='topics'), #route to a users topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'), #route to a specific topic
    path('new_topic/', views.new_topic, name='new_topic'), #route to a new topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), #route to a new entry of a selected topic
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), #editing a selected entry
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:entry_id>/<int:topic_id>/', views.delete_entry, name='delete_entry'),
]


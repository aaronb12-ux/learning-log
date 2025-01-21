from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from rest_framework import viewsets
from .serializers import TopicSerializer, EntrySerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')

@login_required()
def topics(request):
    """Show all topics"""
    user_topics = Topic.objects.filter(owner=request.user).order_by('date_added') #all user topics
    context = {'topics': user_topics} #dictionary of topics
    return render(request, 'learning_logs/topics.html', context)

@login_required()
def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    user_topic = Topic.objects.get(id=topic_id) #user topic. used to get the entries of the specific topic later
    if user_topic.owner != request.user:
        raise Http404
    entries = user_topic.entry_set.order_by('-date_added') #entries of selected topic
    context = {'topic': user_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required()
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        #user wants to create a new topic
        #no data submitted; create a blank form
        form = TopicForm()

    else:
        #data submitted via post; process it
        #request.POST contains all the data sent by the user to the form, gives ability to modify before saving
        form = TopicForm(data=request.POST)
        #information entered by the user
        if form.is_valid():
            #creating a new topic that hasn't been saved to the database
            new_topic = form.save(commit=False)
            #user who made request is owner of the new topic
            new_topic.owner = request.user
            #saving to database
            new_topic.save()
            #user is redirected to the topics page after saving the topic
            #telling Django to reverse-lookup the URL for the 'topics' view in the 'learning_logs' app
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    #sending above form to the template in the context dictionary
    return render(request, 'learning_logs/new_topic.html', context)


@login_required()
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #no data submitted, create a blank form
        form = EntryForm()
    else:
        #POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #protecting page so no one can use the URL to gain access to someone elses entries
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required()
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
    if request.method == 'POST':
        topic.delete()
        return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'topic':topic}

    return render(request, 'learning_logs/delete_topic.html', context)

@login_required()
def delete_entry(request, entry_id, topic_id):
    entry = get_object_or_404(Entry, id=entry_id)

    if request.method == 'POST':
        entry.delete()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'entry': entry}
    return render(request, 'learning_logs/delete_entry.html', context)
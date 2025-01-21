from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank registration form
        #if we are not responding to a post request, make an instance of a User creation form
        form = UserCreationForm()
    else:
        #process completed form with data
        form = UserCreationForm(data=request.POST)

        #checking if data is valid
        if form.is_valid():
            #save method returns the newly created user object which is stored in new_user
            new_user = form.save()
            #Log the user in and then redirect to home page

            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)



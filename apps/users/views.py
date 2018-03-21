from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.

# '/' or /users'
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'users/users.html', context)


# '/users/new'
def new(request):
    return render(request, 'users/user_new.html')


# '/users/<id>/edit'
def edit(request, id):
    context = {
        'user_id': id
    }
    return render(request, 'users/user_edit.html', context)


# '/users/<id>'
def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/user.html', context)


# '/users/create', method is 'POST'
def create(request):
    # Validate
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    # Create User object.
    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    return redirect('/users/{}'.format(user.id))


# '/users/<id>/destroy'
def destory(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')


# '/users/<id>/update', method is 'POST'
def update(request, id):
    # Validate
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/{}/edit'.format(id))
    # Update user object. 
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/{}'.format(id))
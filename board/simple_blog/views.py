from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import Category, Subcategory, Topic, Message


def index(request):
    last_updates = Message.objects.order_by('-pub_date')[:5]
    categories = Category.objects.order_by('-pub_date')
    return render(
        request,
        'dashboard/dashboard.html',
        {'categories': categories, 'last_updates': last_updates}
    )


def create_topic(request, subcategory_id):
    topic = Topic(
        name=request.POST['name'],
        description=request.POST['description'],
        subcategory_id=subcategory_id,
    )
    topic.save()

    return HttpResponseRedirect(reverse('topic', args=(topic.id,)))


def create_message(request, topic_id):
    message = Message(
        author=request.POST['author'],
        email=request.POST['email'],
        topic_id=topic_id,
        text=request.POST['text'],
    )
    message.save()

    return HttpResponseRedirect(reverse('topic', args=(topic_id,)))


def subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    if subcategory.category.protected and (not request.user.is_authenticated()):
        messages.error(request, 'You need to be logged in to have access to private topic.')
        return HttpResponseRedirect(reverse('index', args=()))

    return render(request, 'dashboard/subcategory.html', {'subcategory': subcategory})


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if topic.subcategory.category.protected and (not request.user.is_authenticated()):
        messages.error(request, 'You need to be logged in to have access to private topic.')
        return HttpResponseRedirect(reverse('index', args=()))
        
    return render(request, 'dashboard/topic.html', {'topic': topic})


def loginpage_view(request):
    return render(request, 'dashboard/login.html')


def signup_view(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index', args=()))

    return render(request, 'dashboard/login.html', {'error_message': 'Error during signup'})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index', args=()))

    return render(request, 'dashboard/login.html', {'error_message': 'Error during login'})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index', args=()))

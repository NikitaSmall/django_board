from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

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


class SubcategoryView(generic.DetailView):
    model = Subcategory
    template_name = 'dashboard/subcategory.html'


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'dashboard/topic.html'

from django.shortcuts import render
from stream.models import Stream


def index(request):
    return render(request, 'index.html')


def stream(request):
    return render(request, 'stream.html')


def feed(request):
    objects = Stream.objects.all()[:10]
    context = {
        'objects': objects,
        'title': "Streams feed",
    }
    return render(request, 'feed.html', context)

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def stream(request):
    return render(request, 'stream.html')

def feed(request):
	return render(request, 'feed.html')

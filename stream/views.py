from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib
import http.client
import base64
import json

from cactus import utils
from stream.models import Stream, Statistics
from personal.models import Profile


def index(request):
    return render(request, 'index.html')


def stream(request, pk):
    stream = Stream.objects.get(pk=pk)
    return render(request, 'stream.html', {'object': stream})


def stream_out(request):
    return render(request, 'stream_out.html')


def feed(request):
    objects = Stream.objects.all()[:10]
    context = {
        'objects': objects,
        'title': "Streams feed",
    }
    return render(request, 'feed.html', context)


@csrf_exempt
def validate_photo(request):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': settings.MICROSOFT_API_KEY,
    }
    profile = Profile.objects.get(user=request.user)
    user_face_id = profile.face_id
    data = base64.b64decode(request.POST['image'].split(',')[-1])
    try:
        face_id = utils.get_face_id(data)
    except:
        return HttpResponse(context={'identical': False})

    data = {
        "faceId1": user_face_id,
        "faceId2": face_id
    }
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/verify", str(data), headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data.decode('utf-8'))
        is_ident = data['isIdentical']
        conn.close()
        if is_ident:
            stream = Stream.objects.get(pk=request.POST['object'])
            profile = Profile.objects.get(user=request.user)
            statistics, created = Statistics.objects.get_or_create(stream=stream,
                                                                   user=profile)
            statistics.spent_time += 1
            statistics.save()
        return HttpResponse(json.dumps({'identical': is_ident}),
                            content_type="application/json")
    except Exception:
        return HttpResponse(json.dumps({'identical': False}),
                            content_type="application/json")

    return


@csrf_exempt
def validate_captcha(request):
    data = request.POST
    if 'here' not in data:
        captcha_data = bytes(urllib.parse.urlencode({
            'secret': '6Ldg5x8TAAAAAEStTib3_vUfM5MHM4S4rysu0nt9',
            'response': data['form'].split('=')[-1],
        }).encode())
        result = json.loads(urllib.request.urlopen('https://www.google.com/recaptcha/api/siteverify',
                                                   captcha_data).read().decode('utf-8'))['success']
        if result:
            stream = Stream.objects.get(pk=data['object'])
            profile = Profile.objects.get(user=request.user)
            statistics, created = Statistics.objects.get_or_create(stream=stream,
                                                                   user=profile)
            statistics.spent_time += 3
            statistics.save()
            return HttpResponse(json.dumps({'captcha': True}),
                                content_type="applicration/json")

    return HttpResponse(json.dumps({'captcha': False}),
                        content_type="application/json")

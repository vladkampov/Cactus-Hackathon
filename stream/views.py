from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from personal.models import Profile
import http.client
import base64
import json

from cactus import utils
from stream.models import Stream


def index(request):
    return render(request, 'index.html')


def stream(request):
    return render(request, 'stream.html')


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
        return HttpResponse(context={'identical': "false"})

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
        return HttpResponse(context={'identical': is_ident})
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return

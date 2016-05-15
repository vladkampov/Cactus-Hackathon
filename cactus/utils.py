from django.conf import settings
from django.forms import ValidationError

import json
import http.client
import urllib.request
import urllib.parse
import urllib.error


def get_face_id(data):
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': settings.MICROSOFT_API_KEY,
    }
    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
    })

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/detect?%s" % params, data, headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data.decode('utf-8'))
        if type(data) == list and data:
            face_id = data[0]['faceId']
        else:
            raise ValidationError("Can not recognize face on photo. Upload other avatar.")
        conn.close()
        return face_id
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
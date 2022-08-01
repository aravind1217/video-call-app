from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder

from django.http import JsonResponse
import random
import time

from .models import Member
import json
from django.views.decorators.csrf import csrf_exempt









def getToken(request):
    appId = "dbff31413a4648c88fce2fe6eca3e1a4"
    appCertificate = "e2656c2d948142dbb7b59feb746b25d1"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)
def lobby(request):
    return render(request, 'base/lobby.html')



def room(request):
    return render(request, 'base/room.html')






@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = Member.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = Member.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = Member.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)
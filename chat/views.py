from django.shortcuts import render, redirect
from chat.models import room, message
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def Room(request, R):
    username = request.GET.get('username')
    room_details = room.objects.get(name=R)
    return render(request, 'room.html', {'username': username, 'room': R, 'room_details': room_details})

def checkview(request):
    r = request.POST['room-name']
    u = request.POST['username']

    if room.objects.filter(name = r).exists():
        return redirect('/'+r+'/?username='+u)
    else:
        new_room = room.objects.create(name = r)
        new_room.save()
        return redirect('/'+r+'/?username='+u)

def send(request):
    wmessage = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = message.objects.create(value = wmessage, user=username, room=room_id)
    new_message.save
    return HttpResponse('Message sent')

def getmessages(request, R):
    room_details = room.objects.get(name=R)
    messages = message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
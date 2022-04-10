import time
import datetime
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from sms.forms import MessageForm


# Create your views here.
def index(request):
    return render(request, 'sms/index.html', {'unread_count': 9})


def new_message(request):
    if request.method == 'GET':
        return render(request, 'sms/new_message.html', {'form': MessageForm()})
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print('Sending sms...')
            time.sleep(1)
            print('Message is sent.')
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)('new_message', {'type': 'notify_client', 'message': f'email is sent.{datetime.datetime.now()}'})
        else:
            print('Something is wrong')
            print(form.errors)
        return render(request, 'sms/new_message.html', {'form': MessageForm()})
    else:
        return HttpResponse('Wrong method.')




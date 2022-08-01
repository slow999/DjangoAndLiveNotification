import time
import datetime
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from sms.forms import MessageForm


# Create your views here.
def notification(request):
    return render(request, 'sms/notification.html', {'unread_count': 9})


def send_msg(request):
    if request.method == 'GET':
        return render(request, 'sms/send_msg.html', {'form': MessageForm()})
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print('Sending sms...')
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)('new_message', {'type': 'notify_client', 'message': f'email is sent.{datetime.datetime.now()}'})
            print('Message is sent.')
        else:
            print('Something is wrong')
            print(form.errors)
        return render(request, 'sms/send_msg.html', {'form': MessageForm()})
    else:
        return HttpResponse('Wrong method.')




import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)\
    ('new_message', {'type': 'notify_client', 'message': f'email is sent.{datetime.datetime.now()}'})
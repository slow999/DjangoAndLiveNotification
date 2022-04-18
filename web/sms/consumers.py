import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'new_message'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        pass

    async def notify_client(self, event):
        print(f'Notification consumer ins id {id(self)}')
        print(event)
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))




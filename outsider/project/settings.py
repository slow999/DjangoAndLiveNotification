CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [{'address': ('127.0.0.1', 6666), 'password': 'mypassword'}],
        }
    }
}
wsgi_app = 'mysite.asgi:application'
worker_class = 'uvicorn.workers.UvicornWorker'
workers = 2
bind = 'unix:/tmp/gunicorn/gunicorn-channel.sock'
accesslog = '-'

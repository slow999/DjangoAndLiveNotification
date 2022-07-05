wsgi_app = 'mysite.asgi:application'
worker_class = 'uvicorn.worker.UvicornWorker'
workers = 2
bind = '0.0.0.0:8001'

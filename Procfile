runserver: python manage.py runserver 0.0.0.0:8000
sync: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=sync
gevent: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=gevent
eventlet: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=eventlet
tornado: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=tornado
gthread: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=gthread
gaiohttp: gunicorn worker_benchmark.wsgi --bind=0.0.0.0:8000 --worker-class=gaiohttp

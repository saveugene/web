gunicorn -c /home/box/web/etc/hello.conf.py hello & gunicorn -c /home/box/web/etc/ask.conf.py ask.wsgi

./ask/manage.py syncdb
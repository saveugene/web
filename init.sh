mkdir -p /home/box/web/public/css
mkdir /home/box/web/public/img
mkdir /home/box/web/public/js
mkdir /home/box/web/uploads

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/hello.conf.py /etc/gunicorn.d/hello.conf.py
# sudo ln -sf /home/box/web/etc/ask.conf.py /etc/gunicorn.d/ask.conf.py 

sudo /etc/init.d/nginx restart
# sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

mysql -uroot -e "create database test_db;"

/home/box/web/ask/manage.py makemigrations qa && /home/box/web/ask/manage.py migrate
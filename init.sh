
r=/home/box/web

mkdir -p $r/public/css
mkdir $r/public/img
mkdir $r/public/js
mkdir $r/uploads

sudo ln -sf $r/etc/nginx.conf /etc/nginx/sites-enabled/default
# sudo ln -sf /home/box/web/etc/hello.conf.py /etc/gunicorn.d/hello.conf.py
# sudo ln -sf /home/box/web/etc/ask.conf.py /etc/gunicorn.d/ask.conf.py 

sudo /etc/init.d/nginx restart
# sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

mysql -uroot -e "create database test_db;"

$r/ask/manage.py makemigrations qa && $r/ask/manage.py migrate
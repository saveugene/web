mkdir -p /home/box/web/public/css
mkdir /home/box/web/public/img
mkdir /home/box/web/public/js
mkdir /home/box/web/uploads

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

mysql -uroot -e "create database test_db;"

python3 /home/box/web/ask/manage.py migrate
gunicorn -c /home/box/web/etc/ask.conf.py ask &
gunicorn -c /home/box/web/etc/hello.conf.py hello &
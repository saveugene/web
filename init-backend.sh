while [ ! -d ./ask ]
do
    echo "Waiting app volume to mount"
    sleep 2
done

python3 /home/box/web/ask/manage.py migrate
gunicorn -c /home/box/web/etc/hello.conf.py hello &
python3 /home/box/web/ask/manage.py runserver 0:8000 


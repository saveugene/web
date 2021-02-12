while [ ! -d ./ask ]
do
    echo "Waiting app volume to mount"
    sleep 2
done

# pip_c="$(pip freeze)"
# pip_e="$(cat requirements.txt)"

# if [[ $pip_c =~ $pip_e ]]; then
#     echo "Python libs are up-to-date"
# else
#     pip install -r requirements.txt
# fi


python3 /home/box/web/ask/manage.py runserver 0:8000 &
./ask/manage.py migrate &
gunicorn -c /home/box/web/etc/hello.conf.py hello 

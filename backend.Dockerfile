FROM python:3.4.3

WORKDIR /home/box/web

ADD ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["sh", "init-backend.sh"]
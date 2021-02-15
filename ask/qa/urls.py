from django.conf.urls import url

from .views import test, question, popular, index

urlpatterns = [
    url('popular/', popular),
    url(r'question/(?P<id>[\d]+)', question),
    url('login/', test),
    url('signup/', test),    
    url('ask/',test),
    url('popular/',test),
    url('new/', test),
    url('', index),
]
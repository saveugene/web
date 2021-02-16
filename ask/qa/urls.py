from django.conf.urls import url

from .views import test, question, popular, index, ask

urlpatterns = [
    url('popular/', popular),
    url(r'question/(?P<id>[\d]+)', question),
    url('login/', test),
    url('signup/', test),           
    url('ask/',ask),
    url('new/', test),
    url('', index),
]
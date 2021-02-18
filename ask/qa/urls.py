from django.conf.urls import url

from .views import question, popular, index, ask, login, logout, signup

urlpatterns = [
    url('popular/', popular),
    url(r'question/(?P<id>[\d]+)', question),
    url('login/', login),
    url('logout/', logout),
    url('signup/', signup),           
    url('ask/', ask),
    url('', index),
]
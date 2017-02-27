from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없습니다.
]

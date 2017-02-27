from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elections.urls')), #localhost:8000으로 요청이 들어오면 elections.urls로 전달
    url(r'^admin/', include(admin.site.urls)), #app 접속을 위해 include를 씁니다.
]

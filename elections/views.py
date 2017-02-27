from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate #models에 정의된 Candidate를 import 

def index(request):
    candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러옵니다
    str = "" #마지막에 return해 줄 문자열입니다.
    for candidate in candidates:
        str += "{}기호 {}번 ({})<BR>".format(candidate.name, candidate.party_number, candidate.area) #<BR>은 html에서 다음 줄로 이동하기 위해 쓰입니다.
        str += candidate.introduction + "<P>" #<P>는 html에서 단락을 바꾸기 위해 쓰입니다.
    return HttpResponse(str)

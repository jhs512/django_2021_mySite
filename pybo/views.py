# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. 파이보에 오신것을 환경합니다.")
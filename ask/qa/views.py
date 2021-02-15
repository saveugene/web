
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question as QuestionModel, Answer as AnswerModel
from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def test(request):
    return HttpResponse("Test") 

def question(request, id):
    quest = get_object_or_404(klass=QuestionModel, id=id)
    answrs = AnswerModel.objects.filter(question=quest).all()
    return render(request,'qa/question.html',{
        'question': quest,
        'answers':answrs
    })    


def popular(request):
    page_n = request.GET.get('page', 1)
    qm_list = QuestionModel.objects.popular().all()
    paginator = Paginator(qm_list, 10) 
    page = paginator.page(page_n)
    return render(request,'qa/popular.html',{
        'page': page,
        'page_n_list':range(1, paginator.num_pages+1),
        'detail_page_route':"/question"
    })    


def index(request):
    page_n = request.GET.get('page', 1)
    qm_list = QuestionModel.objects.new().all()
    paginator = Paginator(qm_list, 10) 
    page = paginator.page(page_n)
    return render(request,'qa/index.html',{
        'page': page,
        'page_n_list':range(1,paginator.num_pages+1),
        'detail_page_route':"/question"
    })    
   
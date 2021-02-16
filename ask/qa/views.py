from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question as QuestionModel, Answer as AnswerModel
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import AnswerForm, AskForm



def test(request):
    return HttpResponse("Test") 

@require_http_methods(['GET','POST'])
def question(request, id): 
    quest = get_object_or_404(klass=QuestionModel, id=id)
    answrs = AnswerModel.objects.filter(question=quest).all()
    if request.method == 'GET':
        answer_form = AnswerForm(initial={'question': id})
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save()
    return render(request,'qa/question.html',{
        'question': quest,
        'answers':answrs,
        'form':answer_form
    })



@require_GET
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


@require_GET
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


@require_http_methods(['GET','POST'])
def ask(request):
    if request.method == 'GET':
        form = AskForm()
        return render(request, 'qa/ask.html',{
            "form":form
        })

    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            qst = form.save()
            return HttpResponseRedirect('/question/' + str(qst.id))
        else:
            print('Not valid')
            return render(request, 'qa/ask.html',{
            "form":form
        })

        

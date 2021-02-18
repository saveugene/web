from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods
from .models import Question as QuestionModel, Answer as AnswerModel
from .forms import AnswerForm, AskForm, LoginForm, SignupForm


@login_required(login_url='/login/')
@require_http_methods(['GET','POST'])
def question(request, id):
    quest = get_object_or_404(klass=QuestionModel, id=id)
    if request.method == 'GET':
        answrs = AnswerModel.objects.filter(question=quest).all()
        form = AnswerForm(initial={'question': id})
        return render(request,'qa/question.html',{
            'question': quest,
            'answers':answrs,
            'form':form,
        })
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
        return HttpResponseRedirect('/question/'+str(quest.id))
   

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


@login_required(login_url='/login/')
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
            form._user = request.user
            qst = form.save()
            return HttpResponseRedirect('/question/' + str(qst.id))
        else:
            return render(request, 'qa/ask.html',{
            "form":form
        })


@require_http_methods(['GET','POST'])        
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'qa/login.html',{
            "form": form
        })

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usr = auth.authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if usr is None:
                print('Cant authenticate')
            else:
                auth.login(request, usr)
            return HttpResponseRedirect('/')
            

@require_http_methods(['GET','POST'])        
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            usr = form.save()
            auth.login(request, usr)
            return HttpResponseRedirect('/')

    if request.method == 'GET':
        form = SignupForm()

    return render(request, 'qa/signup.html',{
        "form":form
    })


@login_required()
@require_GET
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

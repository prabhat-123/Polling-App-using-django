from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Question

def home(requests):
    all_questions = Question.objects.all()
    data = {
        'questions_list' : all_questions
    }
    return render(requests, 'polls/index.html', context=data)

def detail(requests,question_id):

    question = Question.objects.get(pk=question_id)
    data = {
        'question': question
    }
    return render(requests, 'polls/detail.html', context=data)

def vote(requests, question_id):
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=requests.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(requests, question_id):
    question = Question.objects.get(pk=question_id)
    data = {
        'question': question
    }
    return render(requests, 'polls/result.html', context=data)
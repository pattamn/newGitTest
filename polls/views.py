from django.shortcuts import render
from django.views.generic import  TemplateView
from django.views import generic
from django.views import View
# Create your views here.
from django.http import HttpResponse
from .models import Choice,Question
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    q = Question.objects.all()
    context_object_name="all_question"
    return render(request,"home.html",{"context":False})


class Home(generic.ListView):
    model=Question
    template_name="home.html"
    def get_query_set(self):
        return Question.objects.all()

class Home1(generic.DetailView):

            model=Choice
            template_name = "home.html"


            #
        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #
        #     return context


class Home(generic.ListView):
    model=Question
    template_name="home.html"
    def get_query_set(self):
        return Question.objects.all()
class QuestionChoice(generic.ListView):
    model=Choice
    template_name = "choice_list.html"
    def get_queryset(self):
        return Choice.objects.filter(post_id=self.kwargs['post_id'])
class Questions(generic.ListView):
    model=Choice
    template_name = "question_choice.html"
    def get_queryset(self):
        return Choice.objects.all()
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     latest_questions_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_questions_list" : latest_questions_list,
#     }
#     return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")[:5]

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist, pai jan :_) ")    
    
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question" : question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question" : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didnot select a choice."
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

    return HttpResponseRedirect (reverse("polls:results", args=(question.id,)))

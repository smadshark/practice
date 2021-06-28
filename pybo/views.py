from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    """
    pybo list
    """
    question_list = Question.objects.order_by('-create_at')
    context = {'question_list': question_list}
    print(question_list)
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question_detail = Question.objects.get(id=question_id)
    question_detail_404 = get_object_or_404(Question, pk=question_id)
    context = {'question': question_detail_404}
    return render(request, 'pybo/question_detail.html', context)

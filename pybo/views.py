from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm


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


def answer_create(req, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if req.method == 'POST':
        form = AnswerForm(req.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_at = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(req, 'pybo/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_at = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()

    return render(request, 'pybo/question_form.html', {'form': form})

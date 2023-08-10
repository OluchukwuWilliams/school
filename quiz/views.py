from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator 
from django.contrib.auth import login, logout, authenticate 
from .models import Subject, Question, Choice, UserChoice
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')

def quiz_home(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/home.html',{'subjects': subjects})

def quiz_page(request, subject_id, page=1):
    subject = Subject.objects.get(pk=subject_id)
    questions = Question.objects.filter(subject=subject)

    paginator = Paginator(questions, 5) 
    page_obj = paginator.get_page(page)

    if request.method =='POST':
        if page_obj.has_next():
            return redirect('quiz_page', subject_id=subject_id, page=page_obj.next_page_number())
        else:
            return redirect('result')
        
    return render(request, 'quiz/page.html', {'subject': subject, 'page_obj': page_obj})


@login_required
def calculate_score(request):
    questions = Question.objects.all()
    score = 0

    if request.method == 'POST':
        for question in questions:
            selected_choice_id = request.POST.get(f'choice_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                UserChoice.objects.create(user=request.user, choice=selected_choice)
                if selected_choice.is_correct:
                    score += 1

        return redirect('result', score=score)

    context = {'questions': questions}
    return render(request, 'quiz/page.html', context)

@login_required
def quiz_result(request, score):
    total_questions = Question.objects.count()
    percentage = (score / total_questions) * 100

    context = {'score': score, 'total_questions': total_questions, 'percentage': percentage}
    return render(request, 'quiz/result.html', context)
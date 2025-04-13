from django.shortcuts import render, redirect
from .models import Mechanics, Thermodynamics, Results
from .forms import Mechanics_Form, Solution_Form, Thermodynamics_Form, User_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
import random
from myapp import answer_db
from myapp import  user_db

def registration(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        name = request.POST.get('user_name')


        if form.is_valid():
            user = user_db.add_users(name)

            return render(request,'start.html',{'name': user.user_name} )

    else:
        form = User_Form()
    return render(request, "registration.html", {'form': form})

def start_page(request):
    user = user_db.get_users()
    return render(request, 'start.html', {'name': user.user_name})


def problem_list(request):
    mechanics_problems = Mechanics.objects.all()
    thermodynamics_problems = Thermodynamics.objects.all()
    return render(request, 'problem_list.html', {'mech_problems': mechanics_problems,'term_problems': thermodynamics_problems})


def add_mechanics_problems(request):
    if request.method == 'POST':
        form = Mechanics_Form(request.POST)
        condition = request.POST.get('condition')
        if form.is_valid():
            if len(condition) > 10:
                form.save()
                return HttpResponseRedirect("/problem_list")
            else:
                return HttpResponseRedirect("/valid_add_mechanics")


    else:
        form = Mechanics_Form()
    return render(request, "add_mechanics.html", {'form': form})

def valid_add_mechanics(request):
    return render(request, "valid_add_mechanics.html")

def add_therm_problems(request):
    if request.method == 'POST':
        form = Thermodynamics_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/problem_list")
    else:
        form = Thermodynamics_Form()
    return render(request, "add_thermodynamics.html", {'form': form})

def start_solution(request):
    return render(request, 'start_solution.html')

def solution_mechanics(request):

    mechanics_problem = Mechanics.objects.all()
    user = user_db.get_users()

    if request.method == 'POST':
        cache.clear()
        form = Solution_Form(request.POST)
        list_of_results = []
        user_answers = request.POST.getlist('answer')
        model_answers = []
        count_of_right_answer = 0
        count_of_answer = 0
        for i in range(len(user_answers)):
            if user_answers[i] == mechanics_problem[i].answer:
                answer = 1
            else:
                answer = 0
            results = Results(number_of_problems = mechanics_problem[i].number,
                              condition = mechanics_problem[i].condition,
                              answer = mechanics_problem[i].answer,
                              user_answer = user_answers[i])
            list_of_results.append(results)
            count_of_right_answer += answer
            count_of_answer += 1
            percent = round(((count_of_right_answer/ count_of_answer) * 100),1)
            model_answers.append( answer_db.db_add_answer(mechanics_problem[i].number, 'm', answer, user.user_id))

        return render(request, 'mechanics_results.html', {'resuls': list_of_results,
                                                          'count_of_right_answer': count_of_right_answer,
                                                          'count_of_answer': count_of_answer,
                                                          'percent':percent})

    else:
        form = Solution_Form()
    return render(request, "solution_mechanics.html", {'problems': mechanics_problem})

def solution_thermodynamics(request):
    user = user_db.get_users()
    thermo_problem = Thermodynamics.objects.all()

    if request.method == 'POST':
        cache.clear()
        form = Solution_Form(request.POST)
        list_of_results = []
        user_answers = request.POST.getlist('answer')
        model_answers = []
        count_of_right_answer = 0
        count_of_answer = 0
        for i in range(len(user_answers)):
            if user_answers[i] == thermo_problem[i].answer:
                answer = 1
            else:
                answer = 0
            results = Results(number_of_problems=thermo_problem[i].number,
                              condition=thermo_problem[i].condition,
                              answer=thermo_problem[i].answer,
                              user_answer=user_answers[i])
            list_of_results.append(results)
            count_of_right_answer += answer
            count_of_answer += 1
            percent = round(((count_of_right_answer / count_of_answer) * 100), 1)
            model_answers.append(answer_db.db_add_answer(thermo_problem[i].number, 't', answer, user.user_id))

        return render(request, 'thermodynamics_results.html', {'resuls': list_of_results,
                                                          'count_of_right_answer': count_of_right_answer,
                                                          'count_of_answer': count_of_answer,
                                                          'percent': percent})
    else:
        form = Solution_Form()
    return render(request, "solution_thermodynamics.html", {'thermo_problem': thermo_problem})

def statistics(request):
    user = user_db.get_users()
    dir_of_stat = answer_db.db_statistics(user.user_id)
    return render(request, 'statistics.html', dir_of_stat)
def delete_answer(request):
    user = user_db.get_users()
    answer_db.db_clear_answer(user.user_id)

    return HttpResponseRedirect("/")

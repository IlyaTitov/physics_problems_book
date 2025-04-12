from myapp.models import Answer, Mechanics

def db_add_answer(number_of_problem, type_of_problem, answer, user_id):

    new_answer = Answer(number_of_problems = number_of_problem, answer = answer, type_of_problem =type_of_problem,  user_id = user_id)
    new_answer.save()
    return new_answer
def db_clear_answer(user):
    Answer.objects.filter(user_id = user).delete()

def db_statistics(user_id):
    user_answer = Answer.objects.filter(user_id = user_id)
    count_answer = user_answer.count()
    right_answer = user_answer.filter(answer = 1)
    count_right_answer = right_answer.count()
    mistake_answer = user_answer.filter(answer = 0)
    count_wrong_answer = mistake_answer.count()
    if count_answer != 0:
        percent_rigth = round(count_right_answer/count_answer * 100, 2)
        percent_wrong = round(count_wrong_answer / count_answer * 100, 2)
    else:
        percent_rigth = 0
        percent_wrong = 0

    count_of_termo = user_answer.filter(type_of_problem = 't').count()
    count_of_mechanics = user_answer.filter(type_of_problem = 'm').count()
    count_of_termo_right =  user_answer.filter(type_of_problem = 't', answer = 1).count()
    count_of_mechanics_right = user_answer.filter(type_of_problem='m', answer=1).count()
    if count_of_termo != 0: percent_thermodynamica =  round(count_of_termo_right/count_of_termo * 100, 2)
    else: percent_thermodynamica = 0
    if count_of_mechanics != 0: percent_mechanics = round(count_of_mechanics_right/count_of_mechanics * 100, 2)
    else: percent_mechanics = 0



    dir_of_statistics = {
        'percent_rigth': percent_rigth,
        'percent_wrong': percent_wrong,
        'count_of_answer': count_answer,
        'count_of_success': count_right_answer,
        'count_of_mistakes': count_wrong_answer,
        'count_of_termo': count_of_termo,
        'count_of_mechanics': count_of_mechanics,
        'count_of_termo_right': count_of_termo_right,
        'count_of_mechanics_right': count_of_mechanics_right,
        'percent_thermodynamica': percent_thermodynamica,
        'percent_mechanics' : percent_mechanics
    }
    return dir_of_statistics
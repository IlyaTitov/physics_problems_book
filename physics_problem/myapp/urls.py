from django.urls import path
from . import views

urlpatterns = [
    path('home', views.start_page, name = 'welcom'),
    path('', views.registration),
    path('problem_list',views.problem_list ),
    path('stat', views.statistics),
    path('add_mechanics', views.add_mechanics_problems),
    path('add_thermodynamics', views.add_therm_problems),
    path('start_solution', views.start_solution),
    path('solution_mechanics', views.solution_mechanics),
    path('solution_thermodynamics',views.solution_thermodynamics),
    path('delete_answer', views.delete_answer)
]
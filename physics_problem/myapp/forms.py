from django import forms
from .models import Mechanics, Answer, Thermodynamics, User

class Mechanics_Form(forms.ModelForm):
    class Meta:
        model = Mechanics
        fields = ['condition', 'answer']
        widgets = {

            'condition': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Условие задачи'
            }),
            'answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ответ'
            })

        }

class Thermodynamics_Form(forms.ModelForm):
    class Meta:
        model = Thermodynamics
        fields = ['condition', 'answer']
        widgets = {

            'condition': forms.Textarea(attrs = {
                'class':'form-control',
                'placeholder': 'Условие задачи'
            }),
            'answer': forms.TextInput(attrs = {
                'class':'form-control',
                'placeholder': 'Ответ'
            }),

        }


class Solution_Form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['number_of_problems', 'answer', 'user_id']
        widgets = {
            'number_of_problems':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер задачи'
            }),
            'answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш Ответ'
            }),
            'user_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш id'
            }),
        }


class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            })
        }
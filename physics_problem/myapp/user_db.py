from myapp.models import User
import sqlite3

def add_users(name):
    User.objects.all().update(flag = 0)
    if not User.objects.filter(user_name = name).exists():
        new_user = User(user_name = name, flag = 1)
        new_user.save()
    else:
        User.objects.filter(user_name = name).update(flag = 1)
    return User(user_name = name)

def get_users():

    User.objects.get(flag = 1)
    return User.objects.get(flag = 1)
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.db import models
#from mfc.models import User
from django.template.context_processors import request

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm



class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/auth/login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()


        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
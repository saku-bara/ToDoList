from dataclasses import field
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import App

class MyLoginView(LoginView):
    template_name = 'myapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class Registration(FormView):
    template_name = 'myapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registration, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registration, self).get(*args, **kwargs)


class DoList(LoginRequiredMixin, ListView):
    model = App 
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(complete=False).count()


       # search_input = self.request.GET.get('search-area') or ''
       # if search_input:
       #     context['tasks'] = context['tasks'].filter(
       #         title__icontains=search_input)

       # context['search_input'] = search_input


        return context

class Details(LoginRequiredMixin, DetailView):
    model = App
    context_object_name = 'task'
    template_name = 'myapp/app.html'

class CreateTask(LoginRequiredMixin, CreateView):
    model = App
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class UpdateData(LoginRequiredMixin, UpdateView):
    model = App
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class DeleteData(LoginRequiredMixin, DeleteView):
    model = App
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
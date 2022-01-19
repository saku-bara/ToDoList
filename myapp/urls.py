from django.urls import path
from .views import DoList, Details, CreateTask, UpdateData, DeleteData, MyLoginView, Registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Registration.as_view(), name='register'),
    path('', DoList.as_view(), name='tasks'),
    path('task/<int:pk>/', Details.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit/<int:pk>/', UpdateData.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteData.as_view(), name='delete'),
]
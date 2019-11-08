"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import (TodoList, todo_detail, TodoCreate, TodoUpdate, TodoDelete,
                    ItemCreate, ItemUpdate, ItemDelete)


urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('create/', TodoCreate.as_view(), name='todo_create'),
    path('<int:pk>/', todo_detail, name='todo_detail'),
    path('<int:pk>/update', TodoUpdate.as_view(), name='todo_update'),
    path('<int:pk>/delete', TodoDelete.as_view(), name='todo_delete'),
    path('item/create/', ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>/update', ItemUpdate.as_view(), name='item_update'),
    path('item/<int:pk>/delete', ItemDelete.as_view(), name='item_delete'),
]

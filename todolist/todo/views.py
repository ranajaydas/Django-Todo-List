from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Todo, Item
from .forms import TodoForm, ItemForm


class TodoCreate(View):
    form_class = TodoForm
    template_name = 'todo/todo_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_todo = bound_form.save()
            return redirect(new_todo)
        else:
            return render(request, self.template_name, {'form': bound_form})


class TodoUpdate(View):
    form_class = TodoForm
    model = Todo
    template_name = 'todo/todo_form_update.html'

    def get(self, request, pk):
        todo = get_object_or_404(self.model, pk=pk)
        context = {
            'form': self.form_class(instance=todo),
            'todo': todo,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        todo = get_object_or_404(self.model, pk=pk)
        bound_form = self.form_class(request.POST, instance=todo)
        if bound_form.is_valid():
            new_todo = bound_form.save()
            return redirect(new_todo)
        else:
            context = {
                'form': bound_form,
                'todo': todo,
            }
            return render(request, self.template_name, context)


class TodoList(View):
    def get(self, request):
        todo_list = Todo.objects.all()
        return render(request, 'todo/todo_list.html', {'todo_list': todo_list})


class TodoDelete(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('todo_list')


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


class ItemCreate(View):
    form_class = ItemForm
    template_name = 'todo/item_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_item = bound_form.save()
            return redirect(new_item)
        else:
            return render(request, self.template_name, {'form': bound_form})


class ItemUpdate(View):
    form_class = ItemForm
    model = Item
    template_name = 'todo/item_form_update.html'

    def get(self, request, pk):
        item = get_object_or_404(self.model, pk=pk)
        context = {
            'form': self.form_class(instance=item),
            'item': item,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        item = get_object_or_404(self.model, pk=pk)
        bound_form = self.form_class(request.POST, instance=item)
        if bound_form.is_valid():
            new_item = bound_form.save()
            return redirect(new_item)
        else:
            context = {
                'form': bound_form,
                'item': item,
            }
            return render(request, self.template_name, context)


class ItemDelete(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'todo/item_confirm_delete.html', {'item': item})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('todo_list')


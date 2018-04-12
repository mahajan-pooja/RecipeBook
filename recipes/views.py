from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe
from .forms import RecipeForm

def index(request):
    recipes = Recipe.objects.all()[:10]

    context = {
        'recipes':recipes
    }
    return render(request, 'index.html', context)

def details(request, id):
    recipe = Recipe.objects.get(id=id)

    context = {
        'recipe':recipe
    }
    return render(request, 'details.html', context)

def delete(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('/recipes')

def edit(request, id):
    recipe = Recipe.objects.get(id=id)

    if(request.method == 'POST'):
        form = RecipeForm(data=request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('/recipes')
    else:
        form = RecipeForm(instance=recipe)
        
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        recipe = Recipe(recipe_name=title, recipe_items=text)
        recipe.save()

        return redirect('/recipes')
    else:
        return render(request, 'add.html')

from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def template_selection(request):
    return render(request, 'coloring/template_selection.html')
    


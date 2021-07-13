from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def main(request):
    return render(request, 'coloring/main.html')


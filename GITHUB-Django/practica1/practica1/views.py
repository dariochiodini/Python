from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html", {})
def portfolio(request):
    return render(request, "portfolio.html", {})
def index(request):
    return render(request, "index.html", {})

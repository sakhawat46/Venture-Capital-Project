from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'venture_app/home.html', context={})


def contact_info(request):
    return render(request, 'venture_app/contact_info.html', context={})


def people(request):
    return render(request, 'venture_app/people.html', context={})


def portfolio(request):
    return render(request, 'venture_app/portfolio.html', context={})


def news(request):
    return render(request, 'venture_app/news.html', context={})


def investment_process(request):
    return render(request, 'venture_app/investment_process.html', context={})
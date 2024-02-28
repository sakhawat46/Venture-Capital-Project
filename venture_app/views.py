from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from venture_app.forms import MemberForm, InvestorForm
from django.contrib import messages
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



def get_investment(request):
    form = MemberForm()
    registered = False
    if request.method == "POST":
        form = MemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
            form = MemberForm()


            # return HttpResponseRedirect(reverse('venture_app:get_investment'))
    diction = {'form':form, 'registered':registered}
    return render(request,'venture_app/get_investment.html', context = diction)



def invest_now(request):
    form = InvestorForm()
    registered = False
    if request.method == "POST":
        form = InvestorForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
            form = InvestorForm()

            # return HttpResponseRedirect(reverse('venture_app:get_investment'))
    diction = {'form':form, 'registered':registered}
    return render(request,'venture_app/invest_now.html', context = diction)
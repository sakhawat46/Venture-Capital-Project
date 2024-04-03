from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from venture_app.forms import MemberForm, InvestorForm
from django.contrib import messages
from venture_app.models import Blog

# Create your views here.


def home(request):
    return render(request, 'venture_app/home.html', context={})


def contact_info(request):
    return render(request, 'venture_app/contact_info.html', context={})


def people(request):
    return render(request, 'venture_app/people.html', context={})


def portfolio(request):
    return render(request, 'venture_app/portfolio.html', context={})


def blog(request):
    all_blog = Blog.objects.all().order_by('-id')
    diction = {'all_blog': all_blog}
    return render(request, 'venture_app/blog.html', context=diction)


def blog_details(request, slug):

    # access package without loop in template
    blog = Blog.objects.get(slug=slug)

    diction = {'blog':blog}
    return render(request, 'venture_app/blog_details.html', context = diction)


def investment_process(request):
    return render(request, 'venture_app/investment_process.html', context={})


def our_purpose(request):
    return render(request, 'venture_app/our_purpose.html', context={})

def our_business(request):
    return render(request, 'venture_app/our_business.html', context={})

def gallery(request):
    return render(request, 'venture_app/gallery.html', context={})


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
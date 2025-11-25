from django.shortcuts import render





def index(request):
    return render(request, 'index.html')



def shop(request):
    return render(request, 'shop.html')




def detail(request):
    return render(request, 'detail.html')


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


def shoping(request):
    return render(request, 'shoping-card.html')


def checkout(request):
    return render(request, 'checkout.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def forget(request):
    return render(request, 'forget_pw.html')

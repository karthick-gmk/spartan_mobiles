from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout as auth_logout
from usermanagement.models.user_model import User
from spartans.models.product_model import product
from spartans.models.master_model import Category,Brand
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'index.html')



def shop(request):
    category_id = request.GET.get('category')
    products = product.objects.select_related('brand', 'category').all()
    categories = Category.objects.all()
    
    if category_id:
        products = products.filter(category_id=category_id)
        brands = Brand.objects.filter(category=category_id)
    else:
        brands = Brand.objects.all()
    
    return render(request, 'shop.html', {'products': products, 'categories': categories, 'brands': brands})




def detail(request, product_id, product_name):
    product_obj = get_object_or_404(product, id=product_id)
    related_products = product.objects.exclude(id=product_obj.id)[:4]
    return render(request, 'detail.html', {'product': product_obj, 'related_products': related_products})



def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


def shoping(request):
    return render(request, 'shoping-card.html')


def checkout(request):
    return render(request, 'checkout.html')


def sign_up(request):
    success_message = None
    if request.method == 'POST':
        print("adfdfd",request.POST)
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city')
        state = request.POST.get('state')
        
        # Validation
        if User.objects.filter(phone=mobile).exists():
            messages.error(request, "Mobile number already registered")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        elif password != cpassword:
            messages.error(request, "Passwords don't match")
        else:
            User.objects.create_user(
                username=email,
                first_name=fullname,
                email=email,
                phone=mobile,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                password=password
            )
            success_message = "Registration successful!"
        return render(request, 'sign_up.html', {'success_message': success_message})
    return render(request, "sign_up.html")


def sign_in(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=fullname)
            if user.check_password(password):
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Password is incorrect")
                return render(request, 'sign_in.html')
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password")
    return render(request, 'sign_in.html')


def forget(request):
    return render(request, 'forget_pw.html')


def logout(request):
    auth_logout(request)
    return redirect('/')

def reset_pw(request):
    return render(request, 'reset_pw.html')
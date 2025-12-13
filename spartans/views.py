from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout as auth_logout
from usermanagement.models.user_model import User
from spartans.models.product_model import product
from spartans.models.master_model import Category,Brand
from django.shortcuts import render, redirect
from spartans.models.service_model import Service, UserRequestService
from spartans.models.master_model import Category, Brand, BrandModel
from spartans.models.product_review_model import ProductReview
from spartans.models.contact_model import Contact
from .models.shop_cart import Cart, Favorite
from django.http import JsonResponse
from spartans.models.check_out_model import Checkout




def index(request):
    products = product.objects.all()[:8]  # First 8 products
    services = Service.objects.all()
    return render(request, 'index.html',{'services': services,'products': products})



def shop(request):
    category_id = request.GET.get('category')
    products = product.objects.all()
    categories = Category.objects.all()

    if category_id:
        products = product.objects.filter(category_id=category_id)
        brands = Brand.objects.filter(category=category_id)
    else:
        brands = Brand.objects.all()

    return render(request, 'shop.html', {'products': products, 'categories': categories, 'brands': brands})



def service_type(request):
    if request.method == 'POST':
        print("service_request",request.POST)
        user_id = request.POST.get('user_id')
        service_id = request.POST.get('service_id')
        category_id = request.POST.get('category_id')
        brand_id = request.POST.get('brand_id')
        brand_model_name = request.POST.get('brand_model_id')  # Text input
        price = request.POST.get('price')
        delivery_date = request.POST.get('delivery_date')

        try:
            # Get or create BrandModel from text input
            brand_model, created = BrandModel.objects.get_or_create(
                name=brand_model_name,
                defaults={'brand_id': brand_id}
            )
            
            user_request = UserRequestService(
                user_id=user_id,
                service_id=service_id,
                category_id=category_id,
                brand_id=brand_id,
                brandModel_id=brand_model.id,  # Use the created/found BrandModel ID
                price=price,
                delivery_date=delivery_date
            )
            user_request.save()
            messages.success(request, "Service request submitted successfully!")   
        except Exception as e:
            print(f"Service-Error: {e}")
            messages.error(request, f"Error: {str(e)}")    
            
    services = Service.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    users = User.objects.all()
    return render(request, 'service_type.html', {'services': services, 'categories':categories ,'brands':brands , 'users':users})


   

def detail(request, product_id, product_name):
    product_obj = product.objects.get(id=product_id)
    related_products = product.objects.exclude(id=product_obj.id)[:4]

    user_review = None
    if request.user.is_authenticated:
        try:
            user_review = ProductReview.objects.get(user=request.user, product=product_obj)
        except ProductReview.DoesNotExist:
            pass

    if request.method == 'POST':
        action = request.POST.get('action', 'create')
        
        if action == 'delete':
            if user_review:
                user_review.delete()
                messages.success(request, "Review deleted successfully!")
            else:
                messages.error(request, "No review found to delete!")
                
        elif action == 'edit':
            rating = request.POST.get('rating')
            review_text = request.POST.get('review')
            
            if not rating or not review_text:
                messages.error(request, "Please provide both rating and review!")
                return redirect(request.path)
            
            if user_review:
                user_review.rating = int(rating)
                user_review.review = review_text
                user_review.save()
                messages.success(request, "Review updated successfully!")
            else:
                messages.error(request, "No review found to edit!")
                
        else:  # create new review
            rating = request.POST.get('rating')
            review_text = request.POST.get('review')
            
            if not rating or not review_text:
                messages.error(request, "Please provide both rating and review!")
                return redirect(request.path)
            
            if user_review:
                messages.error(request, "You have already reviewed this product! You can edit your existing review.")
            else:
                ProductReview.objects.create(
                    user=request.user,
                    product=product_obj,
                    rating=int(rating),
                    review=review_text
                )
                messages.success(request, "Review submitted successfully!")
        return redirect(request.path)
    reviews = ProductReview.objects.filter(product=product_obj).order_by('-created_at')
    return render(request, 'detail.html', {'product': product_obj, 'related_products': related_products,'reviews': reviews,'user_review': user_review})





def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        print("contact", request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        try:
            contact_request = Contact.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                message=message
            )
            contact_request.save()
            messages.success(request, "Message sent successfully!")
            return redirect('/contact')
        except User.DoesNotExist:
            messages.error(request, "Error sending message. Please try again!")
    return render(request, 'contact.html')



def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        print("checkout", request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        try:
            checkout_request = Checkout.objects.create(
                name=name,
                email=email,
                phone=mobile,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                pin_code=pincode
            )
            checkout_request.save()
            cart_items.delete()
            messages.success(request, "Order placed successfully!")
            return redirect('/')
        except User.DoesNotExist:
            messages.error(request, "Error sending message. Please try again!")
    return render(request, 'checkout.html',{'cart_items': cart_items,})


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



def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product_id=product_id,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        messages.success(request, f"{quantity} item(s) added to cart!")
        return redirect('spartans:detail', product_id=product_id, product_name=product.name)
    else:
        messages.error(request, "Please login first!")
        return redirect('spartans:sign_in')


def shoping_card(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        subtotal = sum(item.get_total_price() for item in cart_items)
        print("Cart items:", cart_items)
        return render(request, 'shoping-cart.html', {'cart_items': cart_items,'subtotal': subtotal})
    else:
        messages.error(request, "Please login first!")
        return redirect('spartans:sign_in')   

def remove_cart(request, cart_id):
   cart_item = Cart.objects.get(id=cart_id)
   cart_item.delete()
   return redirect('spartans:shoping_card')



def update_cart_quantity(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        quantity = int(request.POST.get('quantity'))
        
        cart_item = Cart.objects.get(id=cart_id, user=request.user)
        cart_item.quantity = quantity
        cart_item.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def favorites(request):
    if request.user.is_authenticated:
        favorite_items = Favorite.objects.filter(user=request.user)
        print("Favorite items:", favorite_items)
        return render(request, 'favorite.html', {'favorite_items': favorite_items})
    else:
        messages.error(request, "Please login first!")
        return redirect('spartans:sign_in')



def add_to_favorite(request, product_id):
    if request.user.is_authenticated:
        product_obj = product.objects.get(id=product_id)
        favorite_item, created = Favorite.objects.get_or_create(user=request.user,product=product_obj)
        if created:
            messages.success(request, "Product added to favorites!")
        else:
            messages.error(request, "Product is already in favorites!")
        return redirect('spartans:detail', product_id=product_id, product_name=product_obj.name)
    else:
        messages.error(request, "Please login first!")
        return redirect('spartans:sign_in')
    

def remove_favorite(request, favorite_id):
    favorite_item = Favorite.objects.get(id=favorite_id)
    favorite_item.delete()
    return redirect('spartans:favorites')
         




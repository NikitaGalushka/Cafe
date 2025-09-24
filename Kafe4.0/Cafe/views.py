from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DishForm
from django.shortcuts import render, redirect
from django.views import View


# View for adding a new dish
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')  # Update with the page showing all dishes
    else:
        form = DishForm()
    return render(request, 'Cafe/add_dish.html', {'form': form})

class PaymentView(View):
    template_name = "payment.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        card_number = request.POST.get("card_number")
        expiry = request.POST.get("expiry")
        cvc = request.POST.get("cvc")

        if card_number and expiry and cvc:
            return redirect("payment_success")
        return render(request, self.template_name, {"error": "Заполните все поля!"})


def payment_success(request):
    return render(request, "payment_success.html")

# User logout view
def logout_view(request):
    logout(request)
    return redirect('/')


# Add item to cart
def add_to_cart(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)


    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1  # Збільшуємо кількість товару, якщо він уже є
        cart_item.save()

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.items.all()
    else:
        cart_items = []
    return render(request, 'Cafe/cart.html', {'cart_items': cart_items})

# Remove an item from the cart
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')


# View menu with categories and items
def menu_view(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'Cafe/menu.html', {'categories': categories})


def update_cart(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('view_cart')


# List all cafes
def cafe_list(request):
    cafes = Cafe.objects.all()  # Fetch data from the database
    return render(request, 'Cafe/cafe_list.html', {'cafes': cafes})


# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('/')  # Redirect to the homepage
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = AuthenticationForm()

    return render(request, 'Cafe/login.html', {'form': form})


# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("/")  # Redirect to the homepage
    else:
        form = UserCreationForm()

    return render(request, "Cafe/register.html", {"form": form})


# User account page
def account(request):
    return render(request, 'Cafe/account.html')


# Change password view
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Preserve the session after password change
            return redirect('account')  # Redirect to the account page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Cafe/change_password.html', {'form': form})

from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed')

            return render(request, "base.html")
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})


def demo(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/add1')

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')



    return render(request, "login.html")


def add(request):
    return render(request, 'add.html')


def success(request):
    return render(request, 'success.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name,
                                                email=email, )
                user.save();
                print("user created")
        else:
            messages.info(request, "Password Incorrect")
            return redirect('register')
        return render(request, "login.html")
    return render(request, "register.html")

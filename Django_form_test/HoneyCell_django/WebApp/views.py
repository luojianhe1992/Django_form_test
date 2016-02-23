from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)


@login_required
def save_book(request):
    print("in the save_book function")

    context = {}
    errors = []

    context['errors'] = errors
    context['user'] = request.user
    context['book_id'] = request.POST['book_id']
    context['book_name'] = request.POST['book_name']
    context['book_description'] = request.POST['book_description']
    context['book_file'] = request.FILES['book_file']

    if len(Book.objects.filter(user=request.user, book_id=request.POST['book_id'])) != 0:
        print("The book_id already exist, please type in another book_id.")
        errors.append("The book_id already exist, please type in another book_id.")

        return render(request, 'WebApp/message.html', context)

    new_book_instance = Book(user=request.user,
                             book_id=request.POST['book_id'],
                             book_name=request.POST['book_name'],
                             book_description=request.POST['book_description'],
                             book_file=request.FILES['book_file'])
    new_book_instance.save()
    print("new_book_instance save")
    return HttpResponseRedirect(reverse("message"))


from WebApp.forms import *

@login_required
def save_book_using_forms(request):
    print("in the save_book_using_form function")

    context = {}

    errors = []
    context['errors'] = errors

    context['user'] = request.user

    if request.method == "GET":
        print("in the GET method")
        form = BookForm()
        context['form'] = form

        print(form)

        return render(request, 'WebApp/save_book_using_forms.html', context)

    else:
        print("in the POST method")
        form = BookForm(request.POST, request.FILES)
        context['form'] = form

        if not form.is_valid():
            print("The form is not valid.")
            return render(request, 'WebApp/save_book_using_forms.html', context)

        # if you want to access the value of the form, you have to still use request.POST and request.FILES, you can not use form.book_id
        print("*" * 10)
        print(form)
        print("*" * 10)
        print(request.POST['book_id'])
        print("*" * 10)
        print(request.POST['book_name'])
        print("*" * 10)
        print(request.POST['book_description'])
        print("*" * 10)
        print(request.FILES['book_file'])
        print("*" * 10)

        print("^" * 30)

        if len(Book.objects.filter(user=request.user, book_id=request.POST['book_id'])) != 0:
            print("The book_id already exist, please type in another book_id.")
            errors.append()
            print("render back to save_book_using_forms.html, but keep the form.")
            return render(request, 'WebApp/save_book_using_forms.html', context)


        new_book_instance = Book(user=request.user,
                                 book_id=request.POST['book_id'],
                                 book_name=request.POST['book_name'],
                                 book_description=request.POST['book_description'],
                                 book_file=request.FILES['book_file'])

        new_book_instance.save()
        print("already save the new_book_instance")

        return HttpResponseRedirect(reverse('save_book_using_forms'))


@login_required
def show_books(request):
    print("in the show_books function")
    context = {}
    context['user'] = request.user
    books = Book.objects.filter(user=request.user)
    context['books'] = books
    return render(request, 'WebApp/show_books.html', context)

@login_required
def book_detail(request, book_id):
    print("in the book_detail function")
    print(request)
    print(book_id)
    context = {}
    context['user'] = request.user
    book = Book.objects.get(user=request.user, book_id=book_id)
    context['book'] = book
    return render(request, 'WebApp/book_detail.html', context)

@login_required
def delete_book(request, book_id):
    print("in the delete_book function")
    print(request)
    print(book_id)
    context = {}
    context['user'] = request.user
    book = Book.objects.get(user=request.user, book_id=book_id)
    book.delete()
    print("already delete the book")
    return HttpResponseRedirect(reverse("show_books"))




@login_required
def create_new_user_using_forms(request):
    print("in the function create_new_user_using_forms")
    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method")

        form = CreateUserForm()
        context['form'] = form

        print("^" * 30)
        print(form)
        print("^" * 30)

        return render(request, 'WebApp/create_new_user_using_forms.html', context)

    else:
        print("in the POST method")

        form = CreateUserForm(request.POST, request.FILES)
        context['form'] = form

        if not form.is_valid():
            print("The form is not valid.")
            return render(request, 'WebApp/create_new_user_using_forms.html', context)

        print("^" * 30)
        print(form)
        print(request.POST['username'])
        print(request.POST['first_name'])
        print(request.POST['last_name'])
        print(request.POST['email'])
        print(request.POST['password1'])
        print(request.POST['password2'])
        print("^" * 30)

        new_user_instance = User(username=request.POST['username'],
                                 first_name=request.POST['first_name'],
                                 last_name=request.POST['last_name'],
                                 date_joined=datetime.datetime.now(),
                                 email=request.POST['email'],
                                 password=request.POST['password1'])

        new_user_instance.save()
        print("new_user_instance already save.")

        return HttpResponseRedirect(reverse("create_new_user_using_forms"))



@login_required
def show_users(request):
    print("in the show_user function")

    context = {}

    context['user'] = request.user
    users = User.objects.all()
    context['users'] = users

    return render(request, 'WebApp/show_users.html', context)


@login_required
def user_detail(request, user_id):
    print("in the user_detail function")

    print(request)
    print(user_id)

    context = {}
    context['user'] = request.user

    selected_user = User.objects.get(id = user_id)
    context['selected_user'] = selected_user

    print(selected_user)
    print(selected_user.username)
    print(selected_user.first_name)
    print(selected_user.last_name)
    print(selected_user.email)
    print(selected_user.date_joined)

    return render(request, 'WebApp/user_detail.html', context)


@login_required
def delete_user(request, user_id):
    print("in the delete_user function")

    print(request)
    print(user_id)

    context = {}

    context['user'] = request.user

    selected_user = User.objects.get(id = user_id)
    selected_user.delete()
    print("already delete the selected_user")

    return HttpResponseRedirect(reverse("show_users"))




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


@login_required
# This book_id stand for the Book object default id instead of the attribute book_id
def edit_book(request, book_id):
    print("in the edit_book function.")

    print(request)

    print(book_id)

    context = {}

    errors = []

    context['errors'] = errors

    context['user'] = request.user

    if request.method == "GET":

        print("in the GET request of edit_book function")

        # The book_id is the id of the Book object
        book = Book.objects.get(id = book_id)
        context['book'] = book

        print(book.book_id)
        print(book.book_name)
        print(book.book_description)
        print(book.book_file)


        return render(request, 'WebApp/edit_book.html', context)

    else:
        print("in the POST request of edit_book function")

        # The book_id is the id of the Book object
        book = Book.objects.get(id = book_id)
        context['book'] = book

        print(book.book_id)
        print(book.book_name)
        print(book.book_description)
        print(book.book_file)


        if not (request.POST['book_id'] and request.POST['book_name'] and request.POST['book_description'] and request.FILES['book_file']):
            print("There are some field which are None.")
            errors.append("There are some field which are None.")

            return render(request, 'WebApp/edit_book.html', context)

        if (book.book_id != request.POST['book_id']) and (len(Book.objects.filter(book_id=request.POST['book_id'])) > 0):
            print("The book_id already exist.")
            errors.append("The book_id already exist.")

            return render(request, 'WebApp/edit_book.html', context)

        if (book.book_name != request.POST['book_name']) and (len(Book.objects.filter(book_name=request.POST['book_name'])) > 0):
            print("The book_name already exist.")
            errors.append("The book_name already exist.")

            return render(request, 'WebApp/edit_book.html', context)

        if (book.book_description != request.POST['book_description']) and (len(Book.objects.filter(book_description=request.POST['book_description'])) > 0):
            print("The book_description already exist.")
            errors.append("The book_description already exist.")

            return render(request, 'WebApp/edit_book.html', context)

        book.book_id = request.POST['book_id']
        book.book_name = request.POST['book_name']
        book.book_description = request.POST['book_description']
        book.book_file = request.FILES['book_file']
        book.save()
        print("Already change the attribute of book instance")

        print(book.book_id)
        print(book.book_name)
        print(book.book_description)
        print(book.book_file)

        return HttpResponseRedirect(reverse("show_books"))


@login_required
# This book_id stand for the Book object default id instead of the attribute book_id
def edit_book_using_forms(request, book_id):
    print("in the edit_book_using_forms function")

    print(request)
    print(book_id)

    context = {}

    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of edit_book_using_forms")
        book = Book.objects.get(id=book_id)
        context['book'] = book

        # book_data = {'book_id': book.book_id,
        #              'book_name': book.book_name,
        #              'book_description': book.book_description,
        #              'book_file': book.book_file
        #             }
        # initialize the BookForm object
        # form = BookForm(book_data)

        # When you only use BookForm in edit_book_using_forms, you can not keep the original information, you have to create a new blank form.
        form = BookForm()
        print(form)
        context['form'] = form
        return render(request, 'WebApp/edit_book_using_forms.html', context)

    else:
        print("in the POST method of edit_book_using_forms")

        form = BookForm(request.POST, request.FILES)
        context['form'] = form

        book = Book.objects.get(id=book_id)
        context['book'] = book

        # Have to delete the book instance at first, and then create a new instance
        book.delete()
        print("Already delete the book.")

        print(form)

        if not form.is_valid():
            print("The form is not valid.")

            return render(request, 'WebApp/edit_book_using_forms.html', context)
        else:
            print("The form is valid.")

            new_book_instance = Book(user=request.user,
                                     book_id=request.POST['book_id'],
                                     book_name=request.POST['book_name'],
                                     book_description=request.POST['book_description'],
                                     book_file=request.FILES['book_file']
                                     )

            print("%" * 30)
            print(new_book_instance)
            print(new_book_instance.book_id)
            print(new_book_instance.book_name)
            print(new_book_instance.book_description)
            print(new_book_instance.book_file)
            print("%" * 30)

            new_book_instance.save()

            print("Already change the attribute of book instance")

            print(new_book_instance.book_id)
            print(new_book_instance.book_name)
            print(new_book_instance.book_description)
            print(new_book_instance.book_file)

            return HttpResponseRedirect(reverse("show_books"))




@login_required
def edit_book_using_modelform(request, book_id):
    print("in the function of edit_book_using_modelform")

    print(request)

    print(book_id)

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of edit_book_using_modelform function.")

        book = Book.objects.get(id=book_id)
        context['book'] = book

        form = BookModelForm(instance=book)
        context['form'] = form

        return render(request, 'WebApp/edit_book_using_modelform.html', context)

    else:
        print("in the POST method of edit_book_using_modelform function.")

        book = Book.objects.get(id=book_id)
        context['book'] = book

        # Store the original attribute of Book object.
        book_clone = {'book_id': book.book_id,
                      'book_name': book.book_name,
                      'book_description': book.book_description}

        form = BookModelForm(request.POST, request.FILES, instance=book)
        context['form'] = form

        if not form.is_valid():
            print("The BookModelForm is not valid.")
            context['form'] = form
            return render(request, 'WebApp/edit_book_using_modelform.html', context)
        else:
            print("The BookModelForm is valid.")

            if len(Book.objects.filter(book_id=form.cleaned_data.get('book_id'))) == 1:

                print("%" * 40)
                print(book.book_id)
                print(form.cleaned_data.get('book_id'))
                print("%" * 40)

                if book_clone['book_id'] != form.cleaned_data.get('book_id'):
                    print("The book_id already exist.")
                    errors.append("The book_id already exist.")
                    return render(request, 'WebApp/edit_book_using_modelform.html', context)


            if len(Book.objects.filter(book_name=form.cleaned_data.get('book_name'))) == 1:
                if book_clone['book_name'] != form.cleaned_data.get('book_name'):
                    print("The book_name already exist.")
                    errors.append("The book_name already exist.")
                    return render(request, 'WebApp/edit_book_using_modelform.html', context)

            if len(Book.objects.filter(book_description=form.cleaned_data.get('book_description'))) == 1:
                if book_clone['book_description'] != form.cleaned_data.get('book_description'):
                    print("The book_description already exist.")
                    errors.append("The book_description already exist.")
                    return render(request, 'WebApp/edit_book_using_modelform.html', context)

            print(form)
            form.save()
            print("Already save the BookModelForm.")

            return HttpResponseRedirect(reverse('show_books'))



@login_required
def new_message(request):
    print("in the function of new_message.")

    context = {}
    context['user'] = request.user

    return render(request, 'WebApp/new_message.html', context)



def add_memo(request):
    print("in the function of add_memo.")

    context = {}

    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method.")

        return render(request, 'WebApp/add_memo.html', context)

    else:
        print("in the POST method.")

        if not (request.POST['memo_name'] and request.POST['memo_description'] and request.POST['memo_datetime']):
            print("There are some field which are None. Please type in again.")
            errors.append("There are some field which are None. Please type in again.")

            context['memo_name'] = request.POST['memo_name']
            context['memo_description'] = request.POST['memo_description']
            context['memo_datetime'] = request.POST['memo_datetime']

            return render(request, 'WebApp/add_memo.html', context)

        if len(Memo.objects.filter(memo_name=request.POST['memo_name'])):
            print("The memo_name already exist.")
            errors.append("The memo_name already exist.")

            context['memo_name'] = request.POST['memo_name']
            context['memo_description'] = request.POST['memo_description']
            context['memo_datetime'] = request.POST['memo_datetime']

            return render(request, 'WebApp/add_memo.html', context)

        if len(Memo.objects.filter(memo_description=request.POST['memo_description'])):
            print("The memo_description already exist.")
            errors.append("The memo_description already exist.")

            context['memo_name'] = request.POST['memo_name']
            context['memo_description'] = request.POST['memo_description']
            context['memo_datetime'] = request.POST['memo_datetime']

            return render(request, 'WebApp/add_memo.html', context)

        if len(Memo.objects.filter(memo_datetime=request.POST['memo_datetime'])):
            print("The datetime already exist.")
            errors.append("The datetime already exist.")

            context['memo_name'] = request.POST['memo_name']
            context['memo_description'] = request.POST['memo_description']
            context['memo_datetime'] = request.POST['memo_datetime']

            return render(request, 'WebApp/add_memo.html', context)

        new_memo_instance = Memo(user=request.user,
                                 memo_name=request.POST['memo_name'],
                                 memo_description=request.POST['memo_description'],
                                 memo_datetime=request.POST['memo_datetime'])
        new_memo_instance.save()
        print("The new_memo_instance save.")

        return render(request, 'WebApp/add_memo.html', context)

@login_required
def show_memos(request):
    print("in the show_memos function")

    context = {}
    context['user'] = request.user

    memos = Memo.objects.filter(user=request.user)
    context['memos'] = memos

    return render(request, 'WebApp/show_memos.html', context)


@login_required
def add_foo(request):
    print("in the function of add_foo.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_foo function.")

        return render(request, 'WebApp/add_foo.html', context)

    else:
        print("in the POST method of add_foo function.")

        foo_name = request.POST['foo_name']

        if not(foo_name):
            print("There are some fields which are None.")
            errors.append("There are some fields which are None.")

            context['foo_name'] = foo_name

            return render(request, 'WebApp/add_foo.html', context)

        if len(FooModel.objects.filter(foo_name=foo_name)):
            print("The foo_name already exist.")
            errors.append("The foo_name already exist.")

            context['foo_name'] = foo_name

            return render(request, 'WebApp/add_foo.html', context)


        new_foo_instance = FooModel(foo_name=foo_name)
        new_foo_instance.save()
        print("The new_foo_instance already save.")


    return render(request, 'WebApp/add_foo.html', context)


@login_required
def show_foos(request):
    print("in the function of show_foos.")

    context = {}
    context['user'] = request.user

    foos = FooModel.objects.all()
    context['foos'] = foos

    return render(request, 'WebApp/show_foos.html', context)


@login_required
def foo_detail(request, foo_id):
    print("in the function of foo_detail")

    print(request)
    print(foo_id)

    context = {}
    context['user'] = request.user

    foo = FooModel.objects.get(id=foo_id)
    context['foo'] = foo

    return render(request, 'WebApp/foo_detail.html', context)


@login_required
def edit_foo(request, foo_id):
    print("in the function of edit_foo")

    print(request)
    print(foo_id)

    context = {}
    context['user'] = request.user

    if request.method == "GET":
        print("in the GET method of edit_foo function.")

        foo = FooModel.objects.get(id=foo_id)
        context['foo'] = foo

        return render(request, 'WebApp/')
from django import forms
from WebApp.models import *

import datetime

class BookForm(forms.Form):
    book_id = forms.CharField(label="Book id", max_length=100)
    book_name = forms.CharField(label="Book name", max_length=100)
    book_description = forms.CharField(label='Book description', max_length=100)
    book_file = forms.FileField(label="Book file")

    def clean(self):
        cleaned_data = super(BookForm, self).clean()

        book_id = cleaned_data.get('book_id')
        book_name = cleaned_data.get('book_name')
        book_description = cleaned_data.get('book_description')
        book_file = cleaned_data.get('book_file')

        print("&" * 30)
        print(book_id)
        print(book_name)
        print(book_description)
        print(book_file)
        print("&" * 30)

        if not (book_id and book_name and book_description and book_file):
            print("There are some field is None.")
            raise forms.ValidationError("There are some fields which are None.")

        return cleaned_data

    def clean_book_id(self):
        book_id = self.cleaned_data.get('book_id')
        if len(Book.objects.filter(book_id=book_id)):
            raise forms.ValidationError("The book_id already exist.")

        return book_id


class CreateUserForm(forms.Form):
    username = forms.CharField(label='User name')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='User email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean(self):

        print("in the clean function of CreateUserForm class")

        cleaned_data = super(CreateUserForm, self).clean()

        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        date = cleaned_data.get('date')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')


        print("^" * 30)
        print(username)
        print(first_name)
        print(last_name)
        print(email)
        print(date)
        print(password1)
        print(password2)
        print("^" * 30)

        if not (password1 == password2):
            print("Password does not match, please type in two passwords again.")
            raise forms.ValidationError("Password does not match, please type in two passwords again.")

        if not (username and first_name and last_name and email and password1 and password2):
            print("There are some fields which are None.")
            raise forms.ValidationError("There are some fields which are None.")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if(len(User.objects.filter(username = username))):
            print("The username already exist.")
            raise forms.ValidationError("The username already exist.")

        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if (len(User.objects.filter(first_name = first_name))):
            print("The first_name already exist.")
            raise forms.ValidationError('The first_name already exist.')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if(len(User.objects.filter(last_name = last_name))):
            print("The last name already exist.")
            raise forms.ValidationError("The last_name already exist.")

        return last_name

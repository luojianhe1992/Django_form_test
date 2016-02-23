from django import forms
from WebApp.models import *


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
            raise forms.ValidationError("There are some field is None.")

        return cleaned_data

    def clean_book_id(self):
        book_id = self.clean_data.get('book_id')
        if len(Book.objects.filter(book_id=book_id)):
            raise forms.ValidationError("The book_id already exist.")

        return book_id
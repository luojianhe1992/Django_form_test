__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views



from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # empty url
    url(r'^$', 'WebApp.views.index', name='index'),

    # new argument 'template_name'
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'WebApp/login.html'}, name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'WebApp.views.my_logout', name='logout'),

    # registration is normal route
    url(r'^registration/$', 'WebApp.views.registration', name='registration'),

    # after login, show the message page to the user
    url(r'^message/$', 'WebApp.views.message', name='message'),

    # go to upload page
    url(r'^upload/$', 'WebApp.views.upload', name='upload'),

    # go to preprocess page
    url(r'preprocess/$', 'WebApp.views.preprocess', name='preprocess'),

    # go to visualization page
    url(r'visualization/$', 'WebApp.views.visualization', name='visualization'),

    # go to honeycell page
    url(r'honeycell/$', 'WebApp.views.honeycell', name='honeycell'),

    # go to honeycomb page
    url(r'honeycomb/$', 'WebApp.views.honeycomb', name='honeycomb'),

    # go to analytics page
    url(r'analytics/$', 'WebApp.views.analytics', name='analytics'),

    url(r'save_book/$', 'WebApp.views.save_book', name='save_book'),

    url(r'show_books/$', 'WebApp.views.show_books', name='show_books'),

    url(r'book_detail/(?P<book_id>\d+)$', 'WebApp.views.book_detail', name='book_detail'),

    url(r'delete_book/(?P<book_id>\d+)$', 'WebApp.views.delete_book', name='delete_book'),

    url(r'save_book_using_forms/$', 'WebApp.views.save_book_using_forms', name='save_book_using_forms'),

    url(r'create_new_user_using_forms/$', 'WebApp.views.create_new_user_using_forms', name='create_new_user_using_forms'),

    url(r'show_users/$', 'WebApp.views.show_users', name='show_users'),

    url(r'user_detail/(?P<user_id>\d+)$', 'WebApp.views.user_detail', name='user_detail'),

    url(r'delete_user/(?P<user_id>\d+)$', 'WebApp.views.delete_user', name='delete_user'),

    # This book_id is the Book object default id instead of the attribute book_id
    url(r'edit_book/(?P<book_id>\d+)$', 'WebApp.views.edit_book', name='edit_book'),

    # This book_id is the Book object default id instead of the attribute book_id
    url(r'edit_book_using_forms/(?P<book_id>\d+)$', 'WebApp.views.edit_book_using_forms', name='edit_book_using_forms'),

    # This book_id is the Book object default id instead of the attribute book_id
    url(r'edit_book_using_modelform/(?P<book_id>\d+)$', 'WebApp.views.edit_book_using_modelform', name='edit_book_using_modelform'),

    url(r'new_message/$', 'WebApp.views.new_message', name='new_message'),

    url(r'add_memo/$', 'WebApp.views.add_memo', name='add_memo'),

    url(r'show_memos/$', 'WebApp.views.show_memos', name='show_memos'),

    url(r'add_foo/$', 'WebApp.views.add_foo', name='add_foo'),

    url(r'show_foos/$', 'WebApp.views.show_foos', name='show_foos'),

    # This foo_id is the FooModel object default id instead of the attribute foo_id
    url(r'foo_detail/(?P<foo_id>\d+)$', 'WebApp.views.foo_detail', name='foo_detail'),

    # This foo_id is the FooModel object default id instead of the attribute foo_id
    url(r'edit_foo/(?P<foo_id>\d+)$', 'WebApp.views.edit_foo', name='edit_foo'),

    # This foo_id is the FooModel object default id instead of the attribute foo_id
    url(r'delete_foo/(?P<foo_id>\d+)$', 'WebApp.views.delete_foo', name='delete_foo'),

    # This memo_id is the Memo object default id instead of the attribute memo_id
    url(r'memo_detail/(?P<memo_id>\d+)$', 'WebApp.views.memo_detail', name="memo_detail"),

    # This memo_id is the Memo object default id instead of the attribute memo_id
    url(r'edit_memo/(?P<memo_id>\d+)$', 'WebApp.views.edit_memo', name='edit_memo'),

    # This memo_id is the Memo object default id instead of the attribute memo_id
    url(r'delete_memo/(?P<memo_id>\d+)$', 'WebApp.views.delete_memo', name='delete_memo'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
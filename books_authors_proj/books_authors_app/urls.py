from django.urls import path

from . import views

urlpatterns = [
    path('',views.books),
    path('newbook',views.newbook),
    path('authors',views.authors),
    path('newauthor',views.newauthor),
    path('books/<int:id>',views.book_info),
    path('authors/<int:id>', views.author_info),
    path('addbooktoauthor/<int:id>',views.addbooktoauthor),
    path('addauthortobook/<int:id>', views.addauthortobook),
]

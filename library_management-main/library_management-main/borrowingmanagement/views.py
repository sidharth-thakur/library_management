from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookmanagement.models import Book
from .models import BorrowedBook
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required(login_url='login')
def borrow_book(request, book_id):
    if request.user.is_authenticated and request.user.is_student and not request.user.is_banned:
        num_borrowed_books = BorrowedBook.objects.filter(user=request.user).count()
        if num_borrowed_books < 3:
            book = get_object_or_404(Book, pk=book_id)
            if book.status == 'available':
                BorrowedBook.objects.create(user=request.user, book=book)
                book.status = 'borrowed'
                book.save()
                messages.success(request, 'Book borrowed successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Book is not avialable!')
                return redirect('borrowingmanagement:profile_view')
        else:
            messages.error(request, 'You borrowed max book')
            return redirect('borrowingmanagement:profile_view')
    elif request.user.is_authenticated and request.user.is_banned:
        messages.error(request, 'Sorry u are banned!')
        return redirect('borrowingmanagement:profile_view')

    elif not(request.user.is_authenticated):
       messages.error(request, "you ain't student go back!")
       return redirect('borrowingmanagement:profile_view')

    return redirect('home') 


def profile_view(request):
        user = request.user
        borrowed_books = user.borrowedbook_set.all()
     
        return  render(request, 'borrowingmanagement/borrowbook.html', {'borrowed_books':borrowed_books})
    

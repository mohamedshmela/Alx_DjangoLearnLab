from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html',context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


from django.shortcuts import  redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

#login view

class LoginView(TemplateView):
    template_name= 'relationship_app/login.html'

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # Redirect to a home page
    else:
        form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form':form})
    
#logout view

class LogoutView(TemplateView):
    template_name= 'relationship_app/logout.html'

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

#Registration view

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,'relationship_app/register.html', {'form':form})
    

from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    if user.is_librarian:
        return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
    
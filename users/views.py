from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from homeDir.models import MainPost
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        student_number = request.POST.get('student_number')
        condition_1 = int(student_number[3]) in range(0,2)
        condition_2 = int(student_number[4]) in range(0,10)
        condition_3 = int(student_number[5]) in range(0,1)
        if form.is_valid():
            if '@itu.edu.tr' in email and condition_1 and condition_2 and condition_3:
                form.save()
                messages.success(request, f'Hesabınız oluşturuldu!')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('homepage')
            else:
                messages.warning(request, f'Verileriniz geçersiz! Lütfen Kuralları Okuyunuz')
                return redirect('register')
    else:
        form = UserRegisterForm()

    template = 'users/register.html'

    context = {
    'title':'Kayıt ol',
    'form':form,
    }
    return render(request,template,context)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profiliniz başarıyla güncellendi!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    template = 'users/profile.html'

    total_posts = MainPost.objects.all().count()


    context = {
    'title': 'Profil',
    'u_form': u_form,
    'p_form': p_form,
    'total_posts': total_posts
    }

    return render(request,template,context)

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    template = 'users/change_password.html'
    context = {
    'form':form
    }
    return render(request,template,context)

@login_required
def user_profile(request,username):
    # If no such user exists raise 404
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404

    context = {
    'user': user,
    }

    template = 'users/user_profile.html'
    return render (request, template, context)

class MyPostListView(LoginRequiredMixin,ListView):
    model = MainPost
    template_name = 'users/myposts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20


    def get_context_data(self, **kwargs):
        ctx = super(MyPostListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Paylaşımlarım'
        return ctx
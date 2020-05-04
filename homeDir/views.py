from django.shortcuts import render,reverse,redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import MainPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from comment.models import MainComment
from comment.forms import MainCommentForm
from .forms import MainPostForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def search(request):
    template = 'homeDir/post.html'

    query = request.GET.get('q')
    if query:
        results = MainPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query) | Q(tag__icontains=query))
        count = MainPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query) | Q(tag__icontains=query)).count()
        paginator = Paginator(results, 20)

        page = request.GET.get('page')

        page_obj = paginator.get_page(page)
    else:
        return redirect('homepage')

    context = {
        'posts': page_obj,
        'query':'query',
        'q': query,
        'count': count,
        'page_obj': page_obj,
    }

    return render(request,template,context)

def tag(request):
    template = 'homeDir/tag.html'

    query = request.GET.get('q')
    if query:
        results = MainPost.objects.filter(Q(tag__icontains=query))
        count = MainPost.objects.filter(Q(tag__icontains=query)).count()
        paginator = Paginator(results, 20)

        page = request.GET.get('page')

        page_obj = paginator.get_page(page)
    else:
        return redirect('homepage')
        
    context = {
        'posts': page_obj,
        'q': query,
        'count': count,
        'page_obj': page_obj,
    }

    return render(request,template,context)

class HomeListView(ListView):

    model = MainPost
    template_name = 'homeDir/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']    # for normal view [date_posted]
    paginate_by = 6


    def get_context_data(self, **kwargs):
        ctx = super(HomeListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Ana Sayfa'
        ctx['query'] = 'query'
        ctx['homepage'] = 'homepage'
        return ctx

class PostListView(ListView):

    model = MainPost
    template_name = 'homeDir/post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']    # for normal view [date_posted]
    paginate_by = 12

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Paylaşımlar'
        return ctx


class MainPostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'homeDir/mainpost_form.html'
    form_class = MainPostForm


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = MainPost
    fields = ['title','content','url','tag']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = MainPost
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def mainpost_detail(request,pk):

    post = MainPost.objects.get(pk=pk)
    comment = MainComment.objects.filter(post=pk)

    template = 'homeDir/mainpost_detail.html'
    context = {
        'post':post,
        'comments':comment,
    }

    return render(request, template ,context)



class MainCommentCreateView(LoginRequiredMixin,CreateView):
    template_name = 'comment/maincomment_form.html'
    form_class = MainCommentForm


    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.post = MainPost.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(MainCommentCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Yorum Yap'
        ctx['post'] = MainPost.objects.get(pk=self.kwargs['pk'])
        ctx['comments'] = MainComment.objects.filter(post=self.kwargs['pk'])
        return ctx

    def get_success_url(self):
        return reverse('comment', kwargs={'pk':self.object.post.pk})

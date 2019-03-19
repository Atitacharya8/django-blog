# from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"


class BlogListView(ListView):
    template_name = 'bloglist.html'
    queryset = Blog.objects.all()
    context_object_name = 'bloglist'


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    queryset = Blog.objects.all()
    context_object_name = 'blogdetail'


class BlogCreateView(CreateView):
    template_name = 'blogcreate.html'
    form_class = BlogForm
    success_url = '/blogs/list'


class BlogUpdateView(UpdateView):
    template_name = 'blogupdate.html'
    queryset = Blog.objects.all()
    form_class = BlogForm
    success_url = '/blogs/list/'


class BlogDeleteView(DeleteView):
    template_name = 'blogdelete.html'
    queryset = Blog.objects.all()
    success_url = "/blogs/list/"


def blog_review(req, pk):
    if req.method == "POST":
        form = ReviewForm(req.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created = datetime.datetime.now()
            review.blog = Blog.objects.get(pk=pk)
            review.user = req.user
            review.save()
            messages.success(req, "Review saved Successfully")
        else:
            messages.error(req, "Review not saved")
    return redirect("/blogs/detail/", pk)

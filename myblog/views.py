from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myblog.models import Post, Category
from myblog.forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     return render(request, "home.html")

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    
    # def get_context_data(self, *args, **kwargs):
    #     id_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context['id_menu'] = id_menu
    #     return context


class Article_DetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     id_menu = Category.objects.all()
    #     context = super(Article_DetailView, self).get_context_data(*args, **kwargs)
    #     context['id_menu'] = id_menu
    #     return context

# def CategoryView(request, id):
#     category_posts = Post.objects.filter(category=id.replace('-', ' '))
#     return render(request, "category.html", {
#         'id' : id.title().replace('-', ' '), 'category_posts': category_posts
#     })

class Add_PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = "title, body"

class Add_CategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class Update_PostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

class Delete_PostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myblog.models import Post, Category
from myblog.forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request, "home.html")

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        id_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['id_menu'] = id_menu
        return context


class Article_DetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    def get_context_data(self, *args, **kwargs):
        id_menu = Category.objects.all()
        context = super(Article_DetailView, self).get_context_data(*args, **kwargs)
        l = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = l.total_likes()
        liked = False

        if l.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['id_menu'] = id_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

def CategoryView(request, id):
    category_posts = Post.objects.filter(category=id.replace('-', ' '))
    return render(request, "category.html", {
        'id' : id.title().replace('-', ' '), 'category_posts': category_posts
    })

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

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
    
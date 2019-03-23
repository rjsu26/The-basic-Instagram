from django.views.generic import ListView,CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    # def get_queryset(self):
    #         return Post.objects.order_by('date')
    
class CreatePostView(CreateView):
    model = Post
    template_name = "post.html"
    form_class= PostForm    
    success_url= reverse_lazy('home')

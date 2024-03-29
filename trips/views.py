from django.shortcuts import render
from trips.models import Post


def home(request):
    post_list = Post.objects.all()
    return render(request, 'trips/home.html', {'post_list': post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'trips/post.html', {'post': post})
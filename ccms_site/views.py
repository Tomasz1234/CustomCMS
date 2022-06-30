from django.shortcuts import render, get_object_or_404
from .models import Post, MenuPage
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.views.generic import TemplateView


def framecontent(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    bodies = MenuPage.objects.all()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'framecontent.html',{'posts':posts, 'page':page, 'bodies': bodies})

def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request, 'post_detail.html', {'post':post})


from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Category, Comment
from .forms import BlogPostForm, PostUpdateForm, AuthenticatedCommentForm, AnonymousCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Homepage
def index(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts})
    
# Blog post page
@login_required
def post(request):
    try:
        if request.method == "POST":
            form = BlogPostForm(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()

                return redirect(index)
            
        else:
            form = BlogPostForm()

    except ValueError:
         return render(request, 'blog/post.html', {"form": form, "error": "Error posting your blog"})

    return render(request, 'blog/post.html', {"form": form})

# Search by category
@login_required
def search_by_category(request):
    try:
        category_id = request.GET.get('category')

        if category_id:
            posts = BlogPost.objects.filter(category=category_id)

        else:
            posts = BlogPost.objects.all()

        categories = Category.objects.all()

        context = {
            'posts': posts,
            'categories': categories
        }

    except ValueError:
        return render(request, 'blog/index.html', {"error": "Error searching by category"})

    return render(request, 'blog/search.html', context)

# Blog post details
def post_detail(request, pk):
    post = BlogPost.objects.get(id=pk)

    # Handle form submission
    if request.method == 'POST':
        if request.user.is_authenticated:
            c_form = AuthenticatedCommentForm(request.POST)
        else:
            c_form = AnonymousCommentForm(request.POST)

        #   Check if form is valid
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.post = post

            # Set user if authenticated
            if request.user.is_authenticated:
                comment.user = request.user
                
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        # Initialize empty forms for GET requests
        if request.user.is_authenticated:
            c_form = AuthenticatedCommentForm()
        else:
            c_form = AnonymousCommentForm()

    #   Context for rendering
    context = {
        'post': post,
        'c_form': c_form
    }

    return render(request, 'blog/post_detail.html', context)

# Edit blog post
@login_required
def post_edit(request, pk):
    post = BlogPost.objects.get(id=pk)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
        
    else:
        form = PostUpdateForm(instance=post)

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)

# Delete a blog post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {
        'post': post,
    }

    return render(request, 'blog/post_delete.html', context)
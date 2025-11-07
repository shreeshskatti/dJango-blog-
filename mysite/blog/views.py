from django.views import generic
from django.shortcuts import render
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:5]
        return ctx


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        post = self.object
        ctx['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:5]
        ctx['comments'] = post.comments.filter(active=True)
        # empty form by default
        ctx['comment_form'] = CommentForm()
        ctx['new_comment'] = False
        return ctx

    def post(self, request, *args, **kwargs):
        # Handle comment submission on the same detail page
        self.object = self.get_object()
        form = CommentForm(request.POST)
        context = self.get_context_data(object=self.object)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.object
            new_comment.save()
            # show success note
            context['new_comment'] = True
            context['comment_form'] = CommentForm()  # reset form
        else:
            # return form with errors
            context['comment_form'] = form

        return render(request, self.template_name, context)

from django.shortcuts import redirect, render
from app.models import Article
from .form import CreateArticleForm


def home(request):
    articles = Article.objects.all()
    return render(request, 'app/home.html', {'oi': articles})



def createArticle(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateArticleForm()
    return render(request, 'app/create_article.html', {'form': form})

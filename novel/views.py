from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect, redirect, Http404
from .models import Novel, Chapter, ChapterComment, NovelComment,Haberler,HaberlerComment
from .forums import NovelForm, ChapterForm, NovelCommentForm,ChapterCommentForm,HaberlerForm,HaberlerCommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse


def novel_list(request):
    novels_list = Novel.objects.all()
    query = request.GET.get('q')
    if query:
        novels_list = novels_list.filter(
            Q(title__icontains=query)|
            Q(auth__icontains=query)|
            Q(name__icontains=query)|
            Q(type__icontains=query)|
            Q(genre__icontains=query)|
            Q(tags__icontains=query)|
            Q(league__icontains=query)|
            Q(year__icontains=query)
        ).distinct()

    paginator = Paginator(novels_list, 40) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    novels = paginator.get_page(page_number)

    context={
        'novels':novels,
    }

    return render(request, 'post/index.html', context)

def novel_detail(request, slug):
    novels = get_object_or_404(Novel, slug=slug)
    chapter = novels.Bölümler.all()
    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query)|
                Q(auth__icontains=query)|
                Q(name__icontains=query)|
                Q(type__icontains=query)|
                Q(genre__icontains=query)|
                Q(tags__icontains=query)|
                Q(league__icontains=query)|
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels':novels})


    form = NovelCommentForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.nc_novel = novels
        post.save()
        messages.success(request, 'Yorumunuz yayınlanmıştır')
        return HttpResponseRedirect(novels.get_absolute_url())

    context = {

        'novels' : novels,
        'form':form,
        'chapter' : chapter,

    }
    return render(request,'post/detail.html',context)

def novel_create(request):

    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query)|
                Q(auth__icontains=query)|
                Q(name__icontains=query)|
                Q(type__icontains=query)|
                Q(genre__icontains=query)|
                Q(tags__icontains=query)|
                Q(league__icontains=query)|
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels':novels})

    form = NovelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Seriniz yayınlanmıştır')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form':form,
    }

    return render(request,'post/create.html', context)


"""
Bölüm Viewleri
"""
#def plus(request):
#    b = 16
#    d = request.GET.get('+')
#    if d:
#        b =+ 2
#    elif b == 26:
#        messages.eror(request, 'daha fazla büyütemezsiniz')
#
#    return b


def chapter_detail(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    novel = chapter.novel

    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query) |
                Q(auth__icontains=query) |
                Q(name__icontains=query) |
                Q(type__icontains=query) |
                Q(genre__icontains=query) |
                Q(tags__icontains=query) |
                Q(league__icontains=query) |
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels': novels})


    form = ChapterCommentForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.cc_novel = chapter
        post.save()
        messages.success(request, 'Yorumnuz yayınlanmıştır')
        return HttpResponseRedirect(chapter.get_absolute_url())

    context = {
        'chapter' : chapter,
        'novel' : novel,
        'form' : form,

    }
    return render(request,'post/chapter_detail.html',context)

def chapter_create(request):

    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query)|
                Q(auth__icontains=query)|
                Q(name__icontains=query)|
                Q(type__icontains=query)|
                Q(genre__icontains=query)|
                Q(tags__icontains=query)|
                Q(league__icontains=query)|
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels':novels})

    form = ChapterForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Bölümünüz yayınlanmıştır')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form':form,
    }

    return render(request,'post/create.html', context)

def comment_delete(request, id):
    post = get_object_or_404(ChapterComment, id=id)
    post.delete()
    messages.success(request, 'Yorum silinmiştir')
    return HttpResponseRedirect(post.cc_novel.get_absolute_url())

def ncomment_delete(request, id):

    post = get_object_or_404(NovelComment, id=id)
    post.delete()
    messages.success(request, 'Yorum silinmiştir')
    return HttpResponseRedirect(post.nc_novel.get_absolute_url())

"""Haber Viewlwei"""

def haberler(request):
    haber = Haberler.objects.all()
    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query) |
                Q(auth__icontains=query) |
                Q(name__icontains=query) |
                Q(type__icontains=query) |
                Q(genre__icontains=query) |
                Q(tags__icontains=query) |
                Q(league__icontains=query) |
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels': novels})

    paginator = Paginator(haber, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    haber = paginator.get_page(page_number)   


    context={
        'haber': haber,

    }

    return render(request, 'post/haberler.html',context)

def haberler_detail(request,id):
    haber = get_object_or_404(Haberler, id=id)
    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query) |
                Q(auth__icontains=query) |
                Q(name__icontains=query) |
                Q(type__icontains=query) |
                Q(genre__icontains=query) |
                Q(tags__icontains=query) |
                Q(league__icontains=query) |
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels': novels})

    form = HaberlerCommentForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.hc_haberler = haber
        post.save()
        messages.success(request, 'Yorumunuz yayınlanmıştır')
        return HttpResponseRedirect(haber.get_absolute_url())

    context = {
        'haber':haber,
        'form':form,
    }

    return render(request,'post/haberler_detail.html',context)

def haber_create(request):
    q = request.GET.get('q')
    if q:
        novels_list = Novel.objects.all()
        query = q
        if query:
            novels_list = novels_list.filter(
                Q(title__icontains=query) |
                Q(auth__icontains=query) |
                Q(name__icontains=query) |
                Q(type__icontains=query) |
                Q(genre__icontains=query) |
                Q(tags__icontains=query) |
                Q(league__icontains=query) |
                Q(year__icontains=query)
            ).distinct()

        paginator = Paginator(novels_list, 40)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        novels = paginator.get_page(page_number)

        return render(request, 'post/index.html', {'novels': novels})

    form = HaberlerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.h_user = request.user
        post.save()
        messages.success(request, 'Haberiniz yayınlanmıştır')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/create.html', context)

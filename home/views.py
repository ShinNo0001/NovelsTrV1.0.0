from django.shortcuts import render,HttpResponse
from novel.models import Chapter, Novel,Haberler
from django.core.paginator import Paginator
from django.db.models import Q

def home_view(request):
    chapter_list= Chapter.objects.all()


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

    paginator = Paginator(chapter_list, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    chapter = paginator.get_page(page_number)


    context={
        'chapter':chapter,

    }
    return render(request,'home.html', context)

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Novel(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    img = models.FileField(null=True,blank=True,verbose_name='Resim')
    title = models.CharField(max_length=500, verbose_name='Başlık')
    auth = models.CharField(max_length=100,null=True,blank=True, verbose_name='Yazar')
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name="Diğer Adlar")
    type = models.CharField(max_length=100,verbose_name="Novel Tipi",null=True,blank=True)
    genre = models.CharField(max_length=20,verbose_name="Novel Türü",null=True,blank=True)
    tags = models.CharField(max_length=100,verbose_name='Etiket',null=True,blank=True)
    league = models.CharField(max_length=20,verbose_name="Orjinal Dil",null=True,blank=True)
    year = models.CharField(max_length=5,verbose_name="Yayınlanma Tarihi",null=True,blank=True)
    content = RichTextField(verbose_name='Konu')
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')
    slug = models.SlugField(unique=False, editable=False, max_length=510)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('novel:novel-detail', kwargs={'slug': self.slug})
        #return "/novel/{}".format(self.slug)

    def get_create_url(self):
        return reverse('novel:novel-create')
        #return "/post/{}".format(self.id)

    def get_update_url(self):
        return reverse('novel:novel-update', kwargs={'slug': self.slug})
        #return "/post/{}".format(self.id)

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Novel.objects.filter(slug=unique_slug).exists():
            unique_slug= '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Novel, self).save(*args, **kwargs)

    class Meta:
        ordering = [ 'title', 'id']
        #'-publishing_date'

class Chapter(models.Model):
    novel = models.ForeignKey('novel.Novel', related_name='Bölümler',on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=250, verbose_name='Bölüm İsmi')
    chapter_number = models.CharField(max_length=250,verbose_name='Bölüm Numarası')
    cevirmen = models.CharField(max_length=50, verbose_name='Çevirmen',null=True,blank=True)
    redaktor = models.CharField(max_length=50, verbose_name='Redaktör',null=True,blank=True)
    chapter_content = RichTextField(verbose_name='İçerik')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')
    slug = models.SlugField(unique=True,editable=False, max_length=510,)

    def __str__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse('novel:chapter_detail', kwargs={'slug': self.slug})
        #return "/novel/{}".format(self.slug)

    def get_create_url(self):
        return reverse('novel:chapter-create')
        #return "/post/{}".format(self.id)
    def get_quest(self):
        return reverse('novel:query')

    def get_unique_slug(self):
        slug = slugify(self.chapter_name.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Chapter.objects.filter(slug=unique_slug).exists():
            unique_slug= '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Chapter, self).save(*args, **kwargs)

    class Meta:
        ordering = [ '-created_date', 'id']

class NovelComment(models.Model):
    nc_novel = models.ForeignKey('novel.Novel',related_name="novelcomment",on_delete=models.CASCADE)
    nc_name = models.CharField(max_length=150, verbose_name="İsminiz")
    nc_content = models.TextField(verbose_name="Yorumunuz")
    nc_created_date = models. DateTimeField(auto_now_add=True)

    def get_delete_url(self):
        return reverse('novel:ncommentdelete', kwargs={'id': self.id})

class ChapterComment(models.Model):
    cc_novel = models.ForeignKey('novel.Chapter',related_name="chaptercomment",on_delete=models.CASCADE)
    cc_name = models.CharField(max_length=150, verbose_name="İsminiz")
    cc_content = models.TextField(verbose_name="Yorumunuz")
    cc_created_date = models. DateTimeField(auto_now_add=True)

    def get_delete_url(self):
        return reverse('novel:commentdelete', kwargs={'id': self.id})

class Haberler(models.Model):
    h_user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    h_title = models.CharField(max_length=200,verbose_name='Başlık')
    h_img = models.FileField(null=True,blank=True,verbose_name='Resim')
    h_content = RichTextField(verbose_name='İçerik')
    h_created_date=models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.h_title

    def get_absolute_url(self):
        return reverse('novel:haberler-detail', kwargs={'id': self.id})
        #return "/novel/{}".format(self.slug)

    class Meta:
        ordering = ['-h_created_date']
            #'-publishing_date'

class HaberlerComment(models.Model):
    hc_haberler = models.ForeignKey('novel.Haberler',related_name="haberlercomment",on_delete=models.CASCADE)
    hc_name = models.CharField(max_length=20, verbose_name="Adınız")
    hc_content = models.CharField(max_length=150,verbose_name="Yorumunuz")
    hc_created_date = models. DateTimeField(auto_now_add=True)

    def get_delete_url(self):
        return reverse('novel:commentdelete', kwargs={'id': self.id})

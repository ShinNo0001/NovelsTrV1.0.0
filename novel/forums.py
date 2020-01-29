from django import forms
from .models import *

class NovelForm(forms.ModelForm):

    class Meta:
        model = Novel
        fields = [
            'img',
            'title',
            'auth',
            'name',
            'type',
            'genre',
            'tags',
            'league',
            'year',
            'content',

        ]

class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields =[
            'novel',
            'chapter_name',
            'chapter_number',
            'redaktor',
            'cevirmen',
            'chapter_content',
        ]

class NovelCommentForm(forms.ModelForm):

    class Meta:
        model = NovelComment
        fields =[
            "nc_name",
            "nc_content",
        ]

class ChapterCommentForm(forms.ModelForm):

    class Meta:
        model = ChapterComment
        fields =[
            "cc_name",
            "cc_content",
        ]

class HaberlerForm(forms.ModelForm):

    class Meta:
        model = Haberler
        fields =[
            "h_title",
            "h_img",
            "h_content",
        ]

class HaberlerCommentForm(forms.ModelForm):

    class Meta:
        model = HaberlerComment
        fields =[
            "hc_name",
            "hc_content",
        ]

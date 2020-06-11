from .models import Book, Chapter, Comment, Series
from django import forms


class ChapterForm(forms.ModelForm):
	class Meta:
		model = Chapter
		fields = ['title', 'txt']


class CommentForm(forms.Form):
	comment_text = forms.CharField(widget=forms.Textarea)


class SeriesForm(forms.ModelForm):
	class Meta:
		model = Series
		fields = ["title", "description"]


class BookCreateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', "second_author", "third_author", "description", "price", "tags", "genres", "series"]
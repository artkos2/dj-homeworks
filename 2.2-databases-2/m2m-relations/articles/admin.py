from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                return super().clean() 
            raise ValidationError('Укажите основной раздел')
        return super().clean() 

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


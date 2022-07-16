from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError
from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_category = 0
        categories = []
        for form in self.forms:
            if form.cleaned_data.get('tag'):
                if form.cleaned_data.get('tag').name in categories:
                    raise ValidationError('Разделы дублируются')
                else:
                    categories.append(form.cleaned_data.get('tag').name)
            if form.cleaned_data.get('is_main'):
                main_category += 1

        if main_category > 1:
            raise ValidationError('Основным может только один раздел')
        elif main_category == 0:
            raise ValidationError('Выберите основной раздел')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

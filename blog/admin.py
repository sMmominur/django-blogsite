from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from .models import Category, Post, Tag, Comment
from .mixins.author_mixin import AuthorMixin

class CategoryAdmin(AuthorMixin):
    list_display = ('category_id','name', 'slug', 'status')
    list_display_links = ('name',)
    search_fields = ('name', 'slug')
    list_filter = ('status', 'created_by')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
    actions_on_top = True 
    fields = ('name', 'slug', 'status','category_img')
    actions = ['make_active', 'make_inactive', 'make_draft', 'delete_selected', 'edit_selected', 'select_all']

    def make_active(self, request, queryset):
        queryset.update(status='Active')

    make_active.short_description = 'Mark selected categories as Active'

    def make_inactive(self, request, queryset):
        queryset.update(status='Inactive')

    make_inactive.short_description = 'Mark selected categories as Inactive'

    def make_draft(self, request, queryset):
        queryset.update(status='Draft')

    make_draft.short_description = 'Mark selected categories as Draft'

    def edit_selected(self, request, queryset):
        if queryset.count() == 1:
            # Redirect to the change form for the selected item
            url = reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name),
                          args=[queryset.first().id])
            return HttpResponseRedirect(url)
        else:
            self.message_user(request, _("Please select exactly one item to edit."), level='ERROR')

    edit_selected.short_description = 'Edit selected category'

    def select_all(self, request, queryset):
        queryset.update(is_selected=True)

    select_all.short_description = _('Select all categories')


class PostAdmin(AuthorMixin):
    list_display = ('title', 'author', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'slug')
    list_filter = ('status', 'author', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    actions_on_top = True
    fields = ('category_id','author','title', 'slug', 'main_content', 'status', 'thumbnail', 'uri', 'seo_description')


class TagAdmin(AuthorMixin):
    list_display = ('tag_id', 'tag_name', 'tag_slug', 'created_by', 'updated_by')
    list_display_links = ('tag_name',)
    prepopulated_fields = {'tag_slug': ('tag_name',)}
    fields = ('tag_name', 'tag_slug')


class CommentAdmin(AuthorMixin):
    list_display = ('comment_id', 'post_id', 'author','content')
    fields = ('post_id', 'author', 'content')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

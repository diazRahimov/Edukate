from django.contrib import admin
from .models import Teacher, Subject, Course, Module, Content, Text, File, Video, Image, CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'expertise', 'experience_years', 'is_active', 'created_at')
    search_fields = ('full_name', 'expertise')
    list_filter = ('is_active', 'expertise')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'subject', 'created_at')
    list_filter = ('subject', 'owner')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'overview')
    inlines = [ContentInline]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('module', 'content_type', 'object_id')
    list_filter = ('content_type',)

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'content')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'url')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title',)




@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Admin list page
    list_display = (
        'email',
        'full_name',
        'gender',
        'birth_date',
        'is_staff',
        'is_active',
    )
    list_filter = ('is_staff', 'is_active', 'gender')

    # Admin detail page (edit)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('full_name', 'gender', 'birth_date', 'age')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Create user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'full_name',
                'gender',
                'birth_date',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )

    # Search & ordering
    search_fields = ('email', 'full_name')
    ordering = ('email',)

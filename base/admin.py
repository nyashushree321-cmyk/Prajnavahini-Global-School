from django.contrib import admin

from .models import (
    AfterSchoolProgram,
    Application,
    BlogPost,
    CampusFacility,
    ContactMessage,
    CurricularProgram,
    FAQItem,
    InfraFeature,
    LeaderMessage,
    Mentor,
    OngoingClass,
)


@admin.register(LeaderMessage)
class LeaderMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(InfraFeature)
class InfraFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(AfterSchoolProgram)
class AfterSchoolProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(CampusFacility)
class CampusFacilityAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(CurricularProgram)
class CurricularProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'age_badge', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(OngoingClass)
class OngoingClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'source_page', 'created_at')
    list_filter = ('source_page', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'source_page', 'created_at')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('studentName', 'classApplied', 'academicYear', 'fatherMobile', 'confirmed', 'created_at')
    list_filter = ('confirmed', 'classApplied', 'academicYear')
    search_fields = ('studentName', 'fatherName', 'motherName', 'aadhaar')

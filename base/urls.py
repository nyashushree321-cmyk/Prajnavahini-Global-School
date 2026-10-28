from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('preschool/', views.preschool, name='preschool'),
    path('curricular/', views.curricular, name='curricular'),
    path('facilities/', views.facilities, name='facilities'),
    path('afterschoolprogramme/', views.afterschoolprogramme, name='afterschoolprogramme'),
    path('messages/', views.leader_messages, name='messages'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('login/', views.login_view, name='login'),
    path('application/', views.application_view, name='application'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/final-submit/', views.dashboard_final_submit, name='dashboard_final_submit'),
]

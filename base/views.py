from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ApplicationForm, ContactMessageForm
from .models import (
    AfterSchoolProgram,
    Application,
    BlogPost,
    CampusFacility,
    CurricularProgram,
    FAQItem,
    InfraFeature,
    LeaderMessage,
    Mentor,
    OngoingClass,
)


def _active(model):
    return model.objects.filter(is_active=True)


def index(request):
    context = {
        'infra_features': _active(InfraFeature),
        'leader_messages': _active(LeaderMessage),
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'infra_features': _active(InfraFeature),
        'form': ContactMessageForm(),
    }
    return render(request, 'about.html', context)


def preschool(request):
    context = {
        'curricular_programs': _active(CurricularProgram),
        'ongoing_classes': _active(OngoingClass),
    }
    return render(request, 'preschool.html', context)


def curricular(request):
    context = {
        'curricular_programs': _active(CurricularProgram),
        'ongoing_classes': _active(OngoingClass),
    }
    return render(request, 'curricular.html', context)


def facilities(request):
    context = {
        'facilities': _active(CampusFacility),
    }
    return render(request, 'facilities.html', context)


def afterschoolprogramme(request):
    context = {
        'programs': _active(AfterSchoolProgram),
    }
    return render(request, 'afterschoolprogramme.html', context)


def leader_messages(request):
    context = {
        'leader_messages': _active(LeaderMessage),
    }
    return render(request, 'messages.html', context)


def team(request):
    context = {
        'mentors': _active(Mentor),
    }
    return render(request, 'team.html', context)


def blog(request):
    context = {
        'posts': _active(BlogPost),
    }
    return render(request, 'blog.html', context)


def faq(request):
    context = {
        'faq_items': _active(FAQItem),
        'form': ContactMessageForm(),
    }
    return render(request, 'faq.html', context)


def contact(request):
    context = {
        'form': ContactMessageForm(),
    }
    return render(request, 'contact.html', context)


@require_POST
def contact_submit(request):
    form = ContactMessageForm(request.POST)
    source_page = request.POST.get('source_page', 'contact')
    redirect_map = {
        'about': 'base:about',
        'contact': 'base:contact',
        'faq': 'base:faq',
    }
    redirect_name = redirect_map.get(source_page, 'base:contact')
    if form.is_valid():
        obj = form.save(commit=False)
        obj.source_page = source_page
        obj.save()
        messages.success(request, "Thank you! Your message has been sent. We'll get back to you soon.")
    else:
        messages.error(request, "There was a problem with your submission. Please check the fields and try again.")
    return redirect(redirect_name)


def login_view(request):
    if request.method == 'POST':
        return redirect('base:application')
    return render(request, 'login.html')


def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            request.session['application_id'] = obj.pk
            return redirect('base:dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})


def dashboard_view(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('base:login')
    application = get_object_or_404(Application, pk=application_id)
    return render(request, 'dashboard.html', {'application': application})


@require_POST
def dashboard_final_submit(request):
    application_id = request.session.get('application_id')
    if application_id:
        Application.objects.filter(pk=application_id).update(confirmed=True)
        del request.session['application_id']
    return redirect('base:login')

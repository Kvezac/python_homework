from django.shortcuts import render, get_object_or_404

from .models import Work


def index(request):
    works = Work.objects.all()
    return render(request, 'educational_app/index.html', {'works': works})


def details(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'educational_app/details.html', {'work': work})
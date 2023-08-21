from django.shortcuts import render

from .models import Work


def index(request):
    works = Work.objects.all()
    return render(request, 'educational_app/index.html', {'works': works})

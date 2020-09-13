from django.shortcuts import render
from app01 import models
# Create your views here.


def publishers(request):
    all_publishers = models.publisher.objects.all()
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})

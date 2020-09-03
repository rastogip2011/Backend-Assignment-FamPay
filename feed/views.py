from django.shortcuts import render
from .models import Feed
from .tasks import populate_db
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    pre_task()

    all_videos = Feed.objects.all()

    paginator = Paginator(all_videos, 10)

    page = request.GET.get('page')

    videos = paginator.get_page(page)
    
    return render(request, 'index.html', {'Videos': videos})

def pre_task():
    populate_db()
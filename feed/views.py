from django.shortcuts import render
from .models import Feed
from .tasks import populate_db
from django.core.paginator import Paginator
from background_task.models import Task

# Create your views here.
def index(request):
    
    pre_task(repeat=100)

    all_videos = Feed.objects.all().order_by('-published_at')

    paginator = Paginator(all_videos, 20)

    page = request.GET.get('page')

    videos = paginator.get_page(page)
    
    return render(request, 'index.html', {'Videos': videos})

def pre_task(repeat):

    Task.objects.all().delete()
    populate_db(repeat=repeat)

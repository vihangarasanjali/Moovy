from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the movie by ID
    return render(request, 'movies/detail.html', {'movie': movie})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

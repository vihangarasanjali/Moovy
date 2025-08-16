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
import os
from openai import OpenAI, RateLimitError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chatbot(request):
    response_text = ""
    error_message = None  # to store error info if API fails

    if request.method == "POST":
        user_input = request.POST.get("user_input")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # modern chat model
                messages=[
                    {"role": "system", "content": "You are a helpful movie assistant."},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=150
            )

            response_text = response.choices[0].message.content.strip()

        except RateLimitError:
            error_message = "API quota exceeded. Please check your OpenAI billing."
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"

    return render(request, "movies/chatbot.html", {
        "response_text": response_text,
        "error_message": error_message
    })


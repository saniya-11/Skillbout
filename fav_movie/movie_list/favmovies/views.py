from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'home/movie_list.html', {'movies': movies})

def movie_add_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'home/movie_form.html', {'form': form, 'edit': False})

def movie_edit_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'home/movie_form.html', {'form': form, 'edit': True})

def movie_delete_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'home/movie_delete.html', {'movie': movie})

from django.shortcuts import render, redirect

from .models import Game


def home(request):

    games = Game.objects.all()

    return render(request, 'home.html', {
        'games': games
    })


def add_game(request):

    if request.method == 'POST':

        game_title = request.POST.get('title')

        game_description = request.POST.get('description')

        game_genre = request.POST.get('genre')

        game_release_year = request.POST.get('release_year')

        game_rating = request.POST.get('rating')

        Game.objects.create(
            title=game_title,
            description=game_description,
            genre=game_genre,
            release_year=game_release_year,
            rating=game_rating
        )

        return redirect('home')

    return render(request, 'add_game.html')


def delete_game(request, id):

    game = Game.objects.get(id=id)

    game.delete()

    return redirect('home')


def add_to_cart(request, id):

    game = Game.objects.get(id=id)

    game.is_cart = True

    game.save()

    return redirect('home')
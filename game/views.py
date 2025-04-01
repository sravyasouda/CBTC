from django.shortcuts import render
import random

def play_game(request):
    user_choice = None
    computer_choice = None
    result = None
    image_url = None  # This will store the image URL for the user's choice

    if request.method == 'POST':
        user_choice = request.POST.get('choice')

        # Define image URL based on user's choice
        if user_choice == 'rock':
            image_url = 'rock.png'
        elif user_choice == 'paper':
            image_url = 'paper.png'
        elif user_choice == 'scissors':
            image_url = 'scissors.png'

        # Computer makes a random choice
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        # Determine the result
        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"

    return render(request, 'game/game.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'image_url': image_url
    })
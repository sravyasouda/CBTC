from django.db import models

# Create your models here.
from django.db import models

class GameStats(models.Model):
    user_wins = models.IntegerField(default=0)
    user_losses = models.IntegerField(default=0)
    user_draws = models.IntegerField(default=0)
    computer_wins = models.IntegerField(default=0)
    computer_losses = models.IntegerField(default=0)
    computer_draws = models.IntegerField(default=0)

    def __str__(self):
        return f"User Wins: {self.user_wins}, Computer Wins: {self.computer_wins}"

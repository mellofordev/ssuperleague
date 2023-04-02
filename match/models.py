from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25)
    logo = models.URLField()
    gp = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    gf = models.IntegerField(default=0)
    ga = models.IntegerField(default=0)
    gd = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
class Fixture(models.Model):
    team_name = models.OneToOneField(Team,on_delete=models.CASCADE)
    against_team = models.OneToOneField(Team,on_delete=models.CASCADE,related_name='againstteam')
    round = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.round

class Live(models.Model):
        
    live_team_name = models.OneToOneField(Team,on_delete=models.CASCADE)
    live_against_team = models.OneToOneField(Team,on_delete=models.CASCADE,related_name='liveagainstteam')
    team_score =models.IntegerField(default=0)
    against_team_score = models.IntegerField(default=0)
    is_live=models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.live_team_name)
    
class Highlight(models.Model):
    poster=models.URLField()
    def __str__(self) :
        return (self.id)
class Matchtop(models.Model):
    player=models.CharField(max_length=25)
    image=models.URLField()

    def __str__(self) -> str:
        return str(self.player)
     
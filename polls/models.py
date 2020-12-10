from django.db import models




class RegistrationTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    TeamName = models.CharField(max_length=50)
    TeamMembers = models.CharField(max_length=500)
    Coach = models.CharField(max_length=50)
    Manager = models.CharField(max_length=50)


class TeamMatches(models.Model):
    team_a = models.ForeignKey(
        RegistrationTable, on_delete=models.CASCADE, null=False, blank=False, related_name='teama')
    team_b = models.ForeignKey(
        RegistrationTable, on_delete=models.CASCADE, null=False, blank=False, related_name='teamb')
    venue = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    team_a_points = models.IntegerField(null=True)
    team_b_points = models.IntegerField(null=True)

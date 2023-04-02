from rest_framework import serializers
from .models import *
class LiveSerializer(serializers.ModelSerializer):
    live_team_name = serializers.SerializerMethodField()
    live_against_team = serializers.SerializerMethodField()
    team_logo = serializers.SerializerMethodField()
    against_team_logo = serializers.SerializerMethodField()
    class Meta:
        model = Live
        fields=['live_team_name','live_against_team','team_logo','against_team_logo','team_score','against_team_score','is_live']
    def get_live_team_name(self,obj):
        print(obj)
        return str(obj.live_team_name)
    def get_live_against_team(self,obj):
        return str(obj.live_against_team)
    def get_team_logo(self,obj):
        return str(obj.live_team_name.logo)
    def get_against_team_logo(self,obj):
        return str(obj.live_against_team.logo)
class FixtureSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    against_team = serializers.SerializerMethodField()
    class Meta:
        model = Fixture
        fields=['team_name','against_team','round']
    def get_team_name(self,obj):
        print(obj)
        return str(obj.team_name)
    def get_against_team(self,obj):
        return str(obj.against_team)
class TableSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields=['team_name','gp','w','d','l','gf','ga','gd','points']
    def get_team_name(self,obj):
        print(obj)
        return str(obj.name)

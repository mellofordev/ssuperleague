from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LiveSerializer,FixtureSerializer,TableSerializer
# Create your views here.
@api_view(['GET'])
def live(request):
    live_data = Live.objects.filter(is_live=True)
    data_=[]
    for i in live_data:
         serializer = LiveSerializer(i)
         data_.append(serializer.data)
    return Response({'data':data_})
@api_view(['GET'])
def fixture(request):
    fixture_ = Fixture.objects.all()
    data_=[]
    for i in fixture_:
         for j in i.round:
            serializer = FixtureSerializer(i)
            data_.append(serializer.data)
    return Response({'data':data_})
@api_view(['GET'])
def table(request):
    team_data = Team.objects.all()
    data_dic=[]
    dic_={}
    for i in range(len(team_data)):
        serializers=TableSerializer(team_data[i])
        data_dic.append(serializers.data)
        dic_[i]=data_dic
        data_dic=[]
    print(dic_)
    
    return Response({'data':dic_})
@api_view(['GET'])
def highlights(request):
    images = Highlight.objects.all()
    data_dic=[]
    for i in images:
        data_dic.append(i.poster)

    return Response({'data':data_dic})

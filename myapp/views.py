from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET','Post'])
def UserList (request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    elif request.method == 'Post':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserItem (request , pk):
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExists:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response (serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK )
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)  


@api_view(['GET'])
def Dept (request):
    departments = Department.objects.filter(
        depName = request.data['depName'],
    )
    serializer = DepartmentSerializer(departments , many= True)
    return Response(serializer.data)


@api_view(['GET'])
def Sub (requeset):
    subjects = Subject.objects.filter(
       subName = requeset.data['subName'], 
    )
    serializer = SubjectSerializer(subjects , many = True)
    return Response(serializer.data)

class QList (APIView):
    def Get(request , self):
        ques = Question.objects.all()
        serializer = QuestionSerializer(ques , many = True)
        return Response(serializer.data)
    def Post(request, self):
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


class QItem (APIView):
    def GetItem(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExists:
            raise Http404

    def Get(self, request,pk):
        que = self.get_object(pk)
        serializer = QuestionSerializer(que)
        return Response(serializer.data)
    def Put(self, request,pk):
        que = self.get_object(pk)
        serializer = QuestionSerializer(que, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def Delete(self,request,pk):
        que = self.get_object(pk)
        que.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)






        


    
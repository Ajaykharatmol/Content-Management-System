from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .models import RegisterUser,Task
from rest_framework import generics, status
from .serializers import UserRegisterSerializer,TaskSearchSerializer,TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils import timezone  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q



def index(request):
    return HttpResponse("Hello, world.")


class CreateUserRegister(CreateAPIView):
    model = RegisterUser
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response([serializer.data], status=status.HTTP_200_OK)
            return Response({
                "CreateUser": serializer.data,
                "message": "register successfully!",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        # print(serializer.errors)
        try:
            return Response({'Error': serializer.errors['Email'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            return Response({'Error': serializer.errors['Password2'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            return Response({'Error': serializer.errors['Phone'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        return Response({'Error': "Something Went Wrong !"}, status=status.HTTP_400_BAD_REQUEST)


class AppToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            password = serializer.validated_data['password']

            token, created = Token.objects.get_or_create(user=user)

            registerUser = RegisterUser.objects.filter( Email=token.user).values(
                                                                                                      'Email',
                                                                                                      "Full_Name",
                                                                                                      'Phone')
            # print(registerUser[0])
            context = {"token": token.key,  "Email": registerUser[0]['Email'],
                       "Full_Name": registerUser[0]['Full_Name'],
                       'Phone': registerUser[0]['Phone']
                       }

            #return Response([context], status=status.HTTP_200_OK)
            return Response({
                "Login": context,
                "message": "Login successfully!",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        try:
            return Response({'Error': serializer.errors['non_field_errors'][0]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': "Please Provide Username and Password"}, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse({'message':'ok'}, status=status.HTTP_400_BAD_REQUEST)

   


class AuthorList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchView(generics.ListAPIView):
    def get(self,request):
        query = request.GET.get("search", None)
        data = Task.objects.all()
        
        if query:
           data = data.filter(Q(Title__icontains=query)|Q(Body__icontains=query)|
                              Q(Summary__icontains=query)|Q(Categories__icontains=query)).distinct()
           print(data)
        return Response({"data": TaskSearchSerializer(instance=data, many=True).data })




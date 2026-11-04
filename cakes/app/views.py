from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny

from . models import Cake,Category,Weight,Shape

from . serializers import CakeSerializer,CategorySerializer,WeightSerializer,ShapeSerializer

from authentication.permissions import IsAdmin,IsUser

from rest_framework_simplejwt.authentication import JWTAuthentication

class CakeListCreateView(APIView):

    serializer_class=CakeSerializer

    # authentication_classes=[BasicAuthentication]

    # authentication_classes=[TokenAuthentication]

    authentication_classes=[JWTAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method=='POST':

            permissions=[IsAdmin]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        cakes=Cake.objects.all()

        serializer=self.serializer_class(cakes,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'cake created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class=CakeSerializer

    # authentication_classes=[BasicAuthentication]

    # authentication_classes=[TokenAuthentication]

    authentication_classes=[JWTAuthentication]

    def get_permissions(self):
    
            permissions=[]
    
            if self.request.method in ['PATCH','DELETE']:
    
                permissions=[IsAdmin]
    
            return [permission() for permission in permissions]
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        cake=Cake.objects.get(id=id)

        serializer=self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        cake=Cake.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=cake,partial=True)

        if serializer.is_valid():
                 
            serializer.save()

            data={'msg':'cake updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
            
        cake=Cake.objects.get(id=id)

        cake.delete()

        data={'msg':'cake deleted successfully'}

        return Response(data,status=204)


    
class CategoryListCreateView(APIView):

    serializer_class=CategorySerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method=='POST':

            permissions=[IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        category=Category.objects.all()

        serializer=self.serializer_class(category,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'category created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CategoryRetrieveUpdateDestroyView(APIView):

    serializer_class=CategorySerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):
    
            permissions=[]
    
            if self.request.method in ['PATCH','DELETE']:
    
                permissions=[IsAdminUser]
    
            return [permission() for permission in permissions]
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        category=Category.objects.get(id=id)

        serializer=self.serializer_class(category)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        category=Category.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=category,partial=True)

        if serializer.is_valid():
                 
            serializer.save()

            data={'msg':'category updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
            
        category=Category.objects.get(id=id)

        category.delete()

        data={'msg':'category deleted successfully'}

        return Response(data,status=204)



class ShapeListCreateView(APIView):

    serializer_class=ShapeSerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method=='POST':

            permissions=[IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        shape=Shape.objects.all()

        serializer=self.serializer_class(shape,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'shape created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class ShapeRetrieveUpdateDestroyView(APIView):

    serializer_class=ShapeSerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):
    
            permissions=[]
    
            if self.request.method in ['PATCH','DELETE']:
    
                permissions=[IsAdminUser]
    
            return [permission() for permission in permissions]
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        shape=Shape.objects.get(id=id)

        serializer=self.serializer_class(shape)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        shape=Shape.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=shape,partial=True)

        if serializer.is_valid():
                 
            serializer.save()

            data={'msg':'shape updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
            
        category=Category.objects.get(id=id)

        category.delete()

        data={'msg':'shape deleted successfully'}

        return Response(data,status=204)



class WeightListCreateView(APIView):

    serializer_class=WeightSerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method=='POST':

            permissions=[IsAdminUser]

        return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        weight=Weight.objects.all()

        serializer=self.serializer_class(weight,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'weight created successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class WeightRetrieveUpdateDestroyView(APIView):

    serializer_class=WeightSerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):
    
            permissions=[]
    
            if self.request.method in ['PATCH','DELETE']:
    
                permissions=[IsAdminUser]
    
            return [permission() for permission in permissions]
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        weight=Weight.objects.get(id=id)

        serializer=self.serializer_class(weight)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        weight=Weight.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=weight,partial=True)

        if serializer.is_valid():
                 
            serializer.save()

            data={'msg':'weight updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
            
        weight=Weight.objects.get(id=id)

        weight.delete()

        data={'msg':'weight deleted successfully'}

        return Response(data,status=204)











        



















        















        








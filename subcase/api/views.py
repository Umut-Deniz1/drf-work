from os import name
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from subcase.models import Users, Organizations, Transactions
from subcase.api.serializers import UsersSerializers, OrganizationsSerializers, TransactionsSerializers
import json
import hashlib
from django.utils.crypto import get_random_string


@api_view(["GET", "POST"])
def user_list_create_api_view(request, pk = None):

    if pk is None:
        if request.method == "GET":
            users = Users.objects.all()
            serializer = UsersSerializers(users, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = UsersSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)


    elif pk is not  None and isinstance(pk,int):
        if request.method == "GET":
            users = Users.objects.filter(id=pk)
            serializer = UsersSerializers(users, many=True)
            if serializer.data == []:
                return Response(f"Veritabanında ID = ({pk}) ait kayıt bulunamadı",status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.data)


@api_view(["GET", "POST", "PUT"])
def organization_list_create_api_view(request, pk = None):

    if pk is None:
        if request.method == "GET":
            organizations = Organizations.objects.all()
            serializer = OrganizationsSerializers(organizations, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = OrganizationsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif pk is not  None and isinstance(pk,int):
        try:
            org_instance = Organizations.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(
                {
                    "errors":{
                        "code":404,
                        "message": f"Böyle bir ID ({pk}) ile ilgili organizasyon yok"
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )
        if request.method == "GET":
            organization = Organizations.objects.filter(id=pk)
            serializer = OrganizationsSerializers(organization, many=True)
            if serializer.data == []:
                return Response(f"Veritabanında ID = ({pk}) ait kayıt bulunamadı",status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.data)

        elif request.method == "PUT":
            serializer = OrganizationsSerializers(org_instance, data=request.data)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response("Başarısız",status=status.HTTP_400_BAD_REQUEST)
    
        

@api_view(["GET", "POST", "DELETE"])
def organization_2_users_list_view(request, organization_slug, pk = None):

    if pk is None:
        if request.method == "GET":
            users = Users.objects.all().filter(organizations__slug = organization_slug)
            serializer = UsersSerializers(users, many=True)
            if serializer.data == []:
                return Response(f"Veritabanında Name = ({organization_slug}) ait kayıt bulunamadı",status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.data)

    elif pk is not None and isinstance(pk,int):
        try:
            user_instance = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(
                {
                    "errors":{
                        "code":404,
                        "message": f"Böyle bir ID ({pk}) ile ilgili user yok"
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == "GET":
            users = Users.objects.all().filter(organizations__slug = organization_slug).filter(id=pk)
            serializer = UsersSerializers(users, many=True)
            if serializer.data == []:
                return Response(f"Veritabanında Name = ({organization_slug}) ait kayıt bulunamadı",status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.data)
        
        # elif request.method == "PUT":
        #     serializer = UsersSerializers(user_instance, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            user_instance.delete()
            return Response(
                {
                    "islem":{
                        "code":204,
                        "message": f"ID ({pk}) ile ilgili user silindi"
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            ) 


@api_view(["GET", "POST"])
def genarate_user_token(request, organization_slug, pk):
    if request.method == "GET":
        user = Users.objects.all().filter(organizations__slug = organization_slug).filter(id=pk)
        serializer = UsersSerializers(user, many=True)

        if serializer.data == []:
            return Response(f"Veritabanında ID ({pk}) ile kayıt bulunamadı",status=status.HTTP_204_NO_CONTENT)
        
        
        unique_id = get_random_string(length=32)

        user_instance = Users.objects.get(pk=pk)
        data = {
            "user_name": user_instance.user_name,
            "user_surname": user_instance.user_surname,
            "user_balance": user_instance.user_balance,
            "user_token": unique_id
        }

        serializer = UsersSerializers(user_instance, data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(
            {
                    "islem":{
                        "code":201,
                        "token": unique_id
                    }
                },
                status=status.HTTP_201_CREATED
        )
    

@api_view(["GET", "POST"])
def transaction_deposit(request,organization_slug, pk=None):
    pass




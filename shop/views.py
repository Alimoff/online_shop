from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer
from .serializer import CustomerSerializer
from rest_framework import status

# Create your views here.

class CustomersView(APIView):
    def get(self,request):
        all_customers = Customer.objects.all()
        serialized_data = CustomerSerializer(data=all_customers,many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)
    
    def post(self,request):
        serialized_data = CustomerSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data)
        return Response("error",serialized_data.errors)
    
    def delete(self,request):
        id = request.data['id']

        try:
            Customer.objects.get(id=id).delete()
            return Response({"status":"success"},status=status.HTTP_200_OK)
        except:
            return Response({'status':"not found"},status=status.HTTP_404_NOT_FOUND)

    def patch(self,request):
        customer = Customer.object.get(id=request.data['id'])
        serialized_data = CustomerSerializer(customer,data=request.data,partial=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return  Response(data=serialized_data.data)
        return Response({"error":serialized_data.errors}) 



class SingleCustomer(APIView):
    def get(self,request,id):
        customer_data = Customer.objects.get(id=id)

        return Response(data={
            'id':customer_data.id,
            'name':customer_data.name,
            'email':customer_data.email,
            'password':customer_data.password,
            'adress':customer_data.adress,
            'contact':customer_data.contact,
            'created_at':customer_data.created_at,
            'updated_at':customer_data.updated_at,
        })
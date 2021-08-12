# some basic imports
import json

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate

# rest_framework imports
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

# models.py imports
from .models import ExampleModel
from .serializers import ExampleModelSerializer



# API View to return serialized list of all ExampleModel objects in database
class ExampleModelsList(APIView):
    # for authentication
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # list of all example_model objects in database associated with
        # the user who is requesting to see their example_models
        example_models = ExampleModel.objects.filter(user=request.user)
        # serialize the objects
        serializer = ExampleModelSerializer(example_models, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_example_model(request):

    # get data from request object (what we passed in from the frontend)
    data = request.data

    # get current user
    user = request.user

    # assuming we passed in the correct data from the front end
    ex_int_field = data['ex_int_field']
    ex_char_field = data['ex_char_field']
    ex_text_field = data['ex_text_field']
    ex_bool_field = data['ex_bool_field']

    # create a new model
    # left side is field defined in models.py (i.e. the 'ex_char_field' field)
    # right side is python variable in the backend (i.e. ex_char_field = data['ex_char_field'] is passed in)
    new_example_model = ExampleModel.objects.create(ex_foreign_key=user, ex_int_field=ex_int_field, ex_char_field=ex_char_field, ex_text_field=ex_text_field, ex_bool_field=ex_bool_field)
    new_example_model.save()

    return Response(status=status.HTTP_201_CREATED)

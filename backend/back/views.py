from django.shortcuts import render

# Create your views here.

from back.models import Members
from back.serializers import MemberSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated,) # API授權
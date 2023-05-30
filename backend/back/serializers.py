from rest_framework import serializers
from back.models import Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
        # fields = ('id', 'firstname', 'lastname')
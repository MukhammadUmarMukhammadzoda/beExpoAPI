from rest_framework import serializers
from .models import *  

class AriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ari
        fields = "__all__"

class AsalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asal
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

from rest_framework import serializers
from .models import Parent, Child, Advice, TherapySession, Journal

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'

class TherapySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapySession
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

from rest_framework import generics
from .models import Parent, Child, Advice, TherapySession, Journal
from .serializers import ParentSerializer, ChildSerializer, AdviceSerializer, TherapySessionSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated

class ParentListCreateView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

class ChildListCreateView(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]

class AdviceListView(generics.ListAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    permission_classes = [IsAuthenticated]

class TherapySessionListView(generics.ListAPIView):
    queryset = TherapySession.objects.all()
    serializer_class = TherapySessionSerializer
    permission_classes = [IsAuthenticated]

class JournalListCreateView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

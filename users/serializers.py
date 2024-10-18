from django.shortcuts import render, get_object_or_404
from .models import Parent, Child, Advice, TherapySession, Journal
from django.contrib.auth.decorators import login_required

@login_required
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'parent_list.html', {'parents': parents})

@login_required
def child_list(request):
    children = Child.objects.all()
    return render(request, 'child_list.html', {'children': children})

@login_required
def advice_list(request):
    advice_entries = Advice.objects.all()
    return render(request, 'advice_list.html', {'advice_entries': advice_entries})

@login_required
def therapy_session_list(request):
    therapy_sessions = TherapySession.objects.all()
    return render(request, 'therapy_list.html', {'therapy_sessions': therapy_sessions})

@login_required
def journal_list(request):
    journals = Journal.objects.all()
    return render(request, 'journal_list.html', {'journals': journals})

# Example for viewing a specific child
@login_required
def child_detail(request, child_id):
    child = get_object_or_404(Child, pk=child_id)
    return render(request, 'child.html', {'child': child})










# from rest_framework import serializers
# from .models import Parent, Child, Advice, TherapySession, Journal

# class ParentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parent
#         fields = '__all__'

# class ChildSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Child
#         fields = '__all__'

# class AdviceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advice
#         fields = '__all__'

# class TherapySessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TherapySession
#         fields = '__all__'

# class JournalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Journal
#         fields = '__all__'

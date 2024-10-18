from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Advice, TherapySession,Journal, Child, Parent
from datetime import date
import calendar
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def submit_child_details(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        description = request.POST.get('description')

        # Create and save the child entry
        parent = Parent.objects.get(user=request.user)
        child = Child.objects.create(
            name=name,
            gender=gender,
            description=description
        )
        child.parent.add(parent)

        # Redirect to the same form with feedback
        feedback = f'Child {name} has been successfully registered.'
        return render(request, 'child.html', {'feedback': feedback})

    return render(request, 'child.html')




class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


def activity_view(request, year, month, day):
    current_date = date(year, month, day)
    
    # Fetch advice and therapy session for the current date
    advice = Advice.objects.filter(date=current_date).first()
    therapy_session = TherapySession.objects.filter(date=current_date).first()

    context = {
        'date_info': f"{month}/{day}/{year}",
        'advice_text': advice.advice if advice else 'No advice for today.',
        'therapy_text': therapy_session.therapy_content if therapy_session else 'No therapy session for today.'
    }

    return render(request, 'activity.html', context)


def calendar_view(request, year=None, month=None):
    # If year and month are not provided, use the current month and year
    if not year or not month:
        today = datetime.today()
        year = today.year
        month = today.month

    # Create a calendar object for the specified month and year
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)  # List of weeks, each week is a list of days

    context = {
        'year': year,
        'month': month,
        'calendar': month_days,
    }

    return render(request, 'calendar.html', context)


@login_required
def journal_view(request):
    if request.method == 'POST':
        entry = request.POST.get('entry')
        parent = Parent.objects.get(user=request.user)  # Assuming logged-in user is a parent

        # Retrieve a child (or children) associated with this parent.
        child = Child.objects.filter(parent=parent).first()  # Modify if handling multiple children
        
        # Save the journal entry
        Journal.objects.create(
            child=child,
            parent=parent,
            entry=entry,
            time=timezone.now()
        )
        return redirect('calendar')  # Redirect back to the calendar after saving the entry

    return render(request, 'journal.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Assuming you have a dashboard page
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')






# from django.shortcuts import render,redirect
# from .models import Advice, TherapySession,Journal
# from django.utils.timezone import now

# def activity_view(request, date=None):
#     if date is None:
#         date = now().date()
#     advice = Advice.objects.filter(date=date)
#     therapy_sessions = TherapySession.objects.filter(date=date)
    
#     return render(request, 'activity.html', {'advice': advice, 'therapy_sessions': therapy_sessions})


# from .forms import JournalForm

# def journal_entry_view(request):
#     if request.method == 'POST':
#         form = JournalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('calendar')
#     else:
#         form = JournalForm()
#     return render(request, 'journal.html', {'form': form})













# from rest_framework import generics
# from .models import Parent, Child, Advice, TherapySession, Journal
# from .serializers import ParentSerializer, ChildSerializer, AdviceSerializer, TherapySessionSerializer, JournalSerializer
# from rest_framework.permissions import IsAuthenticated

# class ParentListCreateView(generics.ListCreateAPIView):
#     queryset = Parent.objects.all()
#     serializer_class = ParentSerializer
#     permission_classes = [IsAuthenticated]

# class ChildListCreateView(generics.ListCreateAPIView):
#     queryset = Child.objects.all()
#     serializer_class = ChildSerializer
#     permission_classes = [IsAuthenticated]

# class AdviceListView(generics.ListAPIView):
#     queryset = Advice.objects.all()
#     serializer_class = AdviceSerializer
#     permission_classes = [IsAuthenticated]

# class TherapySessionListView(generics.ListAPIView):
#     queryset = TherapySession.objects.all()
#     serializer_class = TherapySessionSerializer
#     permission_classes = [IsAuthenticated]

# class JournalListCreateView(generics.ListCreateAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer
#     permission_classes = [IsAuthenticated]



from django.urls import path
from .views import ParentListCreateView, ChildListCreateView, AdviceListView, TherapySessionListView, JournalListCreateView

urlpatterns = [
    path('parents/', ParentListCreateView.as_view(), name='parent-list-create'),
    path('children/', ChildListCreateView.as_view(), name='child-list-create'),
    path('advices/', AdviceListView.as_view(), name='advice-list'),
    path('therapies/', TherapySessionListView.as_view(), name='therapy-list'),
    path('journals/', JournalListCreateView.as_view(), name='journal-list-create'),
]

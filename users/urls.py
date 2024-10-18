from django.urls import path
from .views import SignupView,activity_view,calendar_view,journal_view,login_view,submit_child_details

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('activity/<int:year>/<int:month>/<int:day>/', activity_view, name='activity'),
    path('calendar/', calendar_view, name='calendar'),  # current month
    path('calendar/<int:year>/<int:month>/', calendar_view, name='calendar'),  # specific month
    path('journal/', journal_view, name='journal'),
    path('login/', login_view, name='login'),
    path('submit_child_details/', submit_child_details, name='submit_child_details'),
]













# from django.urls import path
# from . import views

# urlpatterns = [
#     path('parents/', views.parent_list, name='parent_list'),
#     path('children/', views.child_list, name='child_list'),
#     path('advice/', views.advice_list, name='advice_list'),
#     path('therapy/', views.therapy_session_list, name='therapy_session_list'),
#     path('journals/', views.journal_list, name='journal_list'),
#     path('child/<int:child_id>/', views.child_detail, name='child_detail'),
# ]


# from django.urls import path
# from .views import ParentListCreateView, ChildListCreateView, AdviceListView, TherapySessionListView, JournalListCreateView

# urlpatterns = [
#     path('parents/', ParentListCreateView.as_view(), name='parent-list-create'),
#     path('children/', ChildListCreateView.as_view(), name='child-list-create'),
#     path('advices/', AdviceListView.as_view(), name='advice-list'),
#     path('therapies/', TherapySessionListView.as_view(), name='therapy-list'),
#     path('journals/', JournalListCreateView.as_view(), name='journal-list-create'),
# ]

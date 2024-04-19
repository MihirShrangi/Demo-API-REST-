from django.urls import path
from . import views , views2

urlpatterns = [
    path('dept',views.DeptListView.as_view()),
    path('dept/<int:pk>',views.DeptDetailView.as_view()),
    path('emp',views2.EmpListView.as_view()),
    path('emp/<int:pk>',views2.EmpDetailsView.as_view()),
]
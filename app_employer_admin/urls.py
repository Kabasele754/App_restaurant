from django.urls import path
from app_employer_admin.views.main_view import DashboradViews

urlpatterns = [
    path("", DashboradViews.as_view(), name="dashboard_employer_admin"),
    ]
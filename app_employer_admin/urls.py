from django.urls import path
from app_employer_admin.views.main_view import DashboradViews
from app_employer_admin.views.manage_food import AddFoodViews
urlpatterns = [
    path("", DashboradViews.as_view(), name="dashboard_employer_admin"),
    path("add-food", AddFoodViews.as_view(), name="add_food"),
]
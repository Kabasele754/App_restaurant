from django.urls import path
from app_client_client.views import IndexclView, Menuview, ProposView,Bookview

urlpatterns = [
    path("", IndexclView.as_view(), name="index"),
    path("menu", Menuview.as_view(), name="menu" ),
    path("propos", ProposView.as_view(), name="propos"),
    path("book",Bookview.as_view(), name="book")
]

# coding: utf-8
from django.urls import path
from order.views import GoodsView

urlpatterns = [
    path('goods', GoodsView.as_view()),
]

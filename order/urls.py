# coding: utf-8
from django.urls import path
from rest_framework.routers import SimpleRouter

from order.views import GoodsView

router = SimpleRouter()
router.register('goods', GoodsView)
urlpatterns = router.urls

# urlpatterns = [
#     path('goods', GoodsView.as_view()),
# ]

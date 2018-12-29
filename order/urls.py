# coding: utf-8
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from order.views import *

router = SimpleRouter()
router.register('goods', GoodsView)
urlpatterns = router.urls

urlpatterns += [
    url('second-kill', SecondKillView.as_view()),
]

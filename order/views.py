# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.redis_prefix import RedisPrefix
from commons.redis_server import redis_cli
from order.models import Goods
from order.serializers import GoodsSerializer


class GoodsView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def retrieve(self, request, *args, **kwargs):
        good = redis_cli.get_instance(RedisPrefix.GOOD.value, kwargs.get('pk'))
        if not good:
            resp = super().retrieve(request, *args, **kwargs)
            redis_cli.set_instance(RedisPrefix.GOOD.value, kwargs.get('pk'), resp.data)
            good = resp.data
        return Response(good)


class SecondKillView(APIView):

    def post(self, request):

        return Response()

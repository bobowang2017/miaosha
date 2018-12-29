# Create your views here.
from rest_framework import mixins, viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.redis_prefix import RedisPrefix
from commons.redis_server import redis_cli
from order.models import Goods, SecondKillOrder
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
        user_info = request.user_info
        good_id = request.data.get('good_id')
        if not good_id:
            raise serializers.ValidationError("参数good_id为空")
        stock = redis_cli.decr_instance(RedisPrefix.GOOD_STOCK.value, good_id)
        if stock < 0:
            raise serializers.ValidationError("秒杀结束")
        count = SecondKillOrder.objects.filter(user_id=user_info.user_id, good_id=good_id).count()
        if count > 0:
            raise serializers.ValidationError("不能重复秒杀")
        # SecondKillOrder.objects.create(user_id=user_info.user_id, good_id=good_id, order_id='')
        return Response('秒杀成功')

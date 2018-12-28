# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Goods
from order.serializers import GoodsSerializer


class GoodsView(APIView):

    def get(self, request):
        goods = Goods.objects.all()
        result = GoodsSerializer(goods, many=True).data
        return Response(result)

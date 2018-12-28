# coding: utf-8
from rest_framework import serializers

from order.models import *


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = "__all__"


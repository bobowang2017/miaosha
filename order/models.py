from django.db import models


class Goods(models.Model):
    good_id = models.CharField('商品编号', max_length=16)
    good_name = models.CharField('商品名称', max_length=32)
    good_title = models.CharField('商品标题', max_length=32)
    good_img = models.CharField('商品图片', max_length=64)
    good_detail = models.CharField('商品详情', max_length=255)
    good_price = models.FloatField('商品价格')
    good_stock = models.IntegerField('商品库存')
    good_extra = models.CharField('备注', max_length=255, null=True)
    create_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = "goods"


class SecondKillGoods(models.Model):
    good_id = models.CharField('商品编号', max_length=16)
    second_kill_price = models.FloatField('商品价格')
    stock_count = models.IntegerField('库存数量')
    start_at = models.DateField('秒杀开始时间')
    end_at = models.DateField('秒杀结束时间')

    class Meta:
        db_table = "second_goods"


class SecondKillOrder(models.Model):
    user_id = models.CharField('用户编号', max_length=16)
    order_id = models.CharField('订单编号', max_length=16)
    good_id = models.CharField('商品编号', max_length=16, unique=True)
    create_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = "second_kill"


class User(models.Model):
    user_id = models.CharField('用户编号', max_length=16)
    nickname = models.CharField('用户昵称', max_length=16)
    password = models.CharField('用户密码', max_length=64)
    salt = models.CharField(max_length=16)
    create_at = models.DateField(auto_now_add=True, null=True)
    update_at = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = "user"


class Order(models.Model):
    ORDER_STATUS = (
        (0, '新建未支付'),
        (1, '待发货'),
        (2, '已发货'),
        (3, '已收货'),
        (4, '已退款'),
        (5, '已完成'),
    )
    user_id = models.CharField('用户编号', max_length=16)
    good_id = models.CharField('商品编号', max_length=16)
    address = models.CharField('收货地址', max_length=255)
    good_name = models.CharField('商品名称', max_length=32)
    good_count = models.IntegerField('商品数量')
    good_price = models.FloatField('商品单价')
    status = models.IntegerField(choices=ORDER_STATUS, default=0)
    create_at = models.DateField(auto_now_add=True, null=True)
    pay_at = models.DateField('支付时间')

    class Meta:
        db_table = "order"

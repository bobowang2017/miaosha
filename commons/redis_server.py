# coding: utf-8
import redis
from miaosha.settings import REDIS_CONFIG

redis_valid_time = 60 * 60


class RedisClient:

    @property
    def redis_client(self):
        pool = redis.ConnectionPool(host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port'])
        client = redis.Redis(connection_pool=pool)
        return client

    def get_instance(self, prefix, key, delete_cache=False):
        """根据key获取value（string类型数据操作）"""
        key = '%s:%s' % (prefix, str(key))
        redis_instance = self.redis_client.get(key)
        if not redis_instance:
            return None
        try:
            res = eval(redis_instance)
        except:
            res = str(redis_instance, encoding='utf-8')
        if delete_cache:
            self.redis_client.delete(key)
        return res

    def set_instance(self, prefix, key, value, default_valid_time=redis_valid_time):
        """设置键值对（string类型数据操作）"""
        key = '%s:%s' % (prefix, str(key))
        self.redis_client.set(key, value, default_valid_time)
        return

    def delete(self, key):
        """删除键值对（string类型数据操作）"""
        self.redis_client.delete(key)
        return

    def incr_instance(self, key, amount=1):
        """根据key自增amount（string类型数据操作）"""
        self.redis_client.incr(key, amount)
        return

    def decr_instance(self, key, amount=1):
        """根据key自减amount（string类型数据操作）"""
        self.redis_client.decr(key, amount)
        return


redis_cli = RedisClient()

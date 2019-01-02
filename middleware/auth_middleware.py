# coding: utf-8
import json

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from commons.redis_prefix import RedisPrefix
from commons.redis_server import redis_cli
from order.models import User
from order.serializers import UserSerializer
import logging

log = logging.getLogger('django')


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        log.info('*' * 60)
        token = request.META.get('HTTP_AUTHORIZATION') or request.META.get('HTTP_TOKEN')
        if not token:
            return HttpResponse(content=json.dumps(dict(code=400, msg='please take your token in header')),
                                content_type='application/json')
        try:
            # user_id = token_auth(token)
            user_info = redis_cli.get_instance(RedisPrefix.USER.value, 'test')
            if not user_info:
                user_info = User.objects.first()
                redis_cli.set_instance(RedisPrefix.USER.value, 'test', UserSerializer(user_info).data)
            request.user_info = user_info
            log.info('=' * 60)
        except Exception as e:
            return HttpResponse(content=json.dumps(dict(code=401, msg='token auth failed')))

# coding: utf-8
import json

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from order.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION') or request.META.get('HTTP_TOKEN')
        if not token:
            return HttpResponse(content=json.dumps(dict(code=400, msg='please take your token in header')),
                                content_type='application/json')
        try:
            # user_id = token_auth(token)
            user_info = User.objects.first()
            request.user_info = user_info
        except Exception as e:
            return HttpResponse(content=json.dumps(dict(code=401, msg='token auth failed')))

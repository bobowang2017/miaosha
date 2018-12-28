# coding: utf-8
import datetime


def compute_run_time(func):
    """
    计算函数运行时间
    :param func:
    :return:
    """
    def _wrapper(request, *args, **kwargs):
        start_at = datetime.datetime.now()
        result = func(request, *args, **kwargs)
        end_at = datetime.datetime.now()
        print((end_at - start_at).seconds)
        return result
    return _wrapper

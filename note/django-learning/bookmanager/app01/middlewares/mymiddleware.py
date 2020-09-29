from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MyMD(MiddlewareMixin):
    def process_request(self, request):
        print(id(request))

    def process_response(self, request, response):
        # print(id(request))
        # print(id(response))
        # ret = HttpResponse('in response')
        return response
        # return ret

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print(callback)
        print(callback_args)
        print(callback_kwargs)
        print('in process view')

    def process_exception(self, request, exception):
        return HttpResponse('异常被process_exception处理了')

    def process_template_response(self,request,response):
        print('in process_template_response')
        return response
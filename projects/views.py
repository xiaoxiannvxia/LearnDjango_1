from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def index(request):
    return HttpResponse('hello')
class IndexView(View):
    def get(self, request):
        # get请求
        return HttpResponse("<h1>GET请求: Hello,  Python测开大佬们!</h1>")
        # 从数据库中读取项目数据
        # datas = [
        #     {
        #         'project_name': '前程贷项目',
        #         'leader': '可优',
        #         'app_name': 'P2P平台应用'
        #     },
        #     {
        #         'project_name': '探索火星项目',
        #         'leader': '优优',
        #         'app_name': '吊炸天应用'
        #     },
        #     {
        #         'project_name': '无比牛逼的项目',
        #         'leader': '可可',
        #         'app_name': '神秘应用'
        #     }
        # ]
        # return render(request, 'index.html', locals())

    # def post(self, request):
    #     return HttpResponse("<h1>POST请求: Hello,  Python测开大佬们!</h1>")
    # def post(self, request):
    #     # 1. json格式的数据存放在body中, 可以使用request.body来获取
    #     import json
    #
    #     # 2. 将bytes类型转化为字符串
    #     one_str = request.body.decode('utf-8')
    #     # 3. json格式的字符串转化为字典
    #     one_dict = json.loads(one_str)
    #     print(type(one_str))
    #     print(one_str)
    #     print(type(one_dict))
    #     print(one_dict)
    #     print(one_dict['name'])
    #
    #     return HttpResponse("<h1>POST请求: Hello,  Python测开大佬们!</h1>")


    def delete(self, request):
        return HttpResponse("<h1>DELETE请求: Hello,  Python测开大佬们!</h1>")

    def put(self, reuqest):
        return HttpResponse("<h1>PUT请求: Hello,  Python测开大佬们!</h1>")
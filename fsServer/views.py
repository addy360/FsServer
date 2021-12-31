from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.index import MyFs

@api_view(['GET'])
def index(request):
    print(type(request))
    context = {
        "author":"addy360",
        "description":"An application api server to view files from a server or any personal computer through any browser"
    }
    return Response(context)

@api_view(['get'])
def directories(request):
    fs = MyFs()

    context = {
        "data":fs.list_dirs()
    }

    return Response(context)

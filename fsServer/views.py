from rest_framework.response import Response
from rest_framework.request import Request
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
def directories(request:Request):
    dir = request.query_params.get('dir')
    fs = MyFs()

    if dir:
        fs.set_path(dir)
        

    context = {
        "directory":fs.get_path(),
        "meta":"directories",
        "data":fs.list_dirs()
    }

    return Response(context)


@api_view(['get'])
def files(request : Request):
    dir = request.query_params.get('dir')
    fs = MyFs()
    if(dir):
        fs.set_path(dir)

    context={
        "meta":"files",
        "directory":fs.get_path(),
        "data":fs.list_files()
    }

    return Response(context)
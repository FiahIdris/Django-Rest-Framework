from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
    body = request.body #byte string of json data
    
   
    data ={}
    try:
        data = json.loads(body)  # json to python dictionary
    except:
        pass
    # print(data)
    data['params'] = dict(request.GET) # url query params
    data['headers'] =dict(request.headers)
    data['content-type'] = request.content_type
    return JsonResponse(data)

from django.http import JsonResponse
import json
from products.models import Product

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data={}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content_type']= model_data.content_type
        data['price'] = model_data.price
    return JsonResponse(data)

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer 


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    
    def perfom_create(self,serializer):
        # serializer.save(user= self.request.user)
        print("======")
        print(serializer.validated_data)
        title= serializer.validated_data.get('title')
        content_type= serializer.validated_data.get('content_type') or None
        if content_type is None:
            content_type = title
        serializer.save(content_type = content_type)
        

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 

product_detail_view = ProductDetailAPIView.as_view()
    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 

product_list_view = ProductListAPIView.as_view()
    
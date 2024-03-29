from rest_framework import serializers 
from .models import Product
from rest_framework.reverse import reverse
from . import validators
 

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field="pk")
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    class Meta:
        model=Product
        fields=[
           'user','edit_url','url','pk', #'email',
           'title', 'content_type','price', 'sale_price','my_discount'
        ]
    # 
    # def create(self,validated_data):
    #     obj = super().create(validated_data)
    #     return obj
    # 
    # def update(self,validated_data):
    #     email = validated_data.pop('email') 
    #     obj = super().update(validated_data)
    #     return obj
        
    # def validate_title(self,value):
    #     qs= Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already product name.")
    #     return value
    
    def get_edit_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={'pk':obj.pk},request=request)
      
    def get_my_discount(self,obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
from rest_framework import fields, serializers
from .models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('name', 'description', 'price')
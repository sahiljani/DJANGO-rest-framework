from rest_framework import serializers
from .models import ListingDetail 

class ListingDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListingDetail
        fields = ['title']
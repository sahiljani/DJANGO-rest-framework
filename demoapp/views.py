from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . models import ListingDetail
from . serializers import ListingDetailSerializer

# Create your views here.

@api_view(['GET',])
def view_listing_details(request, lid):
	try:
		listing_details = ListingDetail.objects.get(id=lid)
	except ListingDetail.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = ListingDetailSerializer(listing_details)
		return Response(serializer.data)

@api_view(['PUT',])
def update_listing_details(request, lid):
	try:
		listing_details = ListingDetail.objects.get(id=lid)
	except ListingDetail.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "PUT":
		serializer = ListingDetailSerializer(listing_details, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["success"] = "update success"
			return Response(data=data)

		return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)


@api_view(['DELETE',])
def delete_listing_details(request, lid):
	try:
		listing_details = ListingDetail.objects.get(id=lid)
	except ListingDetail.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	data = {}
	if request.method == "DELETE":
		operation = listing_details.delete()
		if operation:
			data["success"] = "delete success"
			return Response(data=data)

		return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)



@api_view(['POST'])
def add_listing_details(request):
	data = {}
	if request.method == "POST":
		listing_details = ListingDetail()
		serializer = ListingDetailSerializer(listing_details, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
from django.urls import path,include
from .views import view_listing_details,update_listing_details, delete_listing_details,add_listing_details

urlpatterns = [
	path('add/',add_listing_details, name="delete details"),
	path('<lid>/',view_listing_details, name="listing details"),
	path('update/<lid>/',update_listing_details, name="update details"),
	path('delete/<lid>/',delete_listing_details, name="delete details"),

]

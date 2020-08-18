from django.contrib import admin
from useradmission.models import *

# register your models here.
admin.site.site_header = "Rental Auction Admin ";
admin.site.site_title = "Admin";

class PropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ['propid','propname','regdate','verifystatus']
    list_filter = ['regdate','verifystatus']

admin.site.register(AddressDetails)
admin.site.register(UserDetails)
admin.site.register(PropertyDetails,PropertyDetailsAdmin)
admin.site.register(PropertyAmenities)
admin.site.register(PropRooms)
admin.site.register(PropertyRented)
admin.site.register(RentReceipt)
admin.site.register(AuctionInfo)
admin.site.register(BidRecords)
admin.site.register(TourBooking)
admin.site.register(UserContactNumber)
admin.site.register(PropertyImages)
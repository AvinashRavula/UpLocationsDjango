from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from RestAPIs.rest_apis.ContactDetails import ContactDetailsViewSet
from RestAPIs.rest_apis.EmailIds import EmailIdsViewSet
from RestAPIs.rest_apis.Floor import FloorViewSet
from RestAPIs.rest_apis.PhoneNumbers import PhoneNumbersViewSet
from RestAPIs.rest_apis.PriceType import PriceTypeViewSet
from RestAPIs.rest_apis.ProfilePicture import ProfilePictureViewSet
from RestAPIs.rest_apis.SocialContacts import SocialContactsViewSet
from RestAPIs.rest_apis.SocialNames import SocialNamesViewSet
from RestAPIs.rest_apis.Socials import SocialsViewSet
from RestAPIs.rest_apis.Table import TableViewSet
from RestAPIs.rest_apis.UserProfiles import UserProfilesViewSet
from RestAPIs.rest_apis.Venues import VenuesViewSet

router = routers.DefaultRouter()
router.register('venues', VenuesViewSet, 'venues')
router.register('user_profiles', UserProfilesViewSet, 'user_profiles')
router.register('socials', SocialsViewSet, 'socials')
router.register('social_names', SocialNamesViewSet, 'social_names')
router.register('social_contacts', SocialContactsViewSet, 'social_contacts')
router.register('profile_picture', ProfilePictureViewSet, 'profile_picture')
router.register('price_type', PriceTypeViewSet, 'price_type')
router.register('phone_numbers', PhoneNumbersViewSet, 'phone_numbers')
router.register('email_ids', EmailIdsViewSet, 'email_ids')
router.register('contact_details', ContactDetailsViewSet, 'contact_details')
router.register('tables', TableViewSet, 'tables')
router.register('floors', FloorViewSet, 'floors')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]

from django.urls import path

from .views import HomePageView,brandsPageView,categoryPageView,productPageView,gettingFormDetails,getDetails,dashBoard
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('auth', gettingFormDetails, name='auth'),
    path('login', getDetails, name='login'),
    path('category', categoryPageView.as_view(), name='category'),
    path('products', productPageView.as_view(), name='products'),
    path('brands', brandsPageView.as_view(), name='brands'),
    path('dashBoard',dashBoard,name="dashBoard"),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
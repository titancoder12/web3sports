"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapi import views


# https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
# https://adiramadhan17.medium.com/modify-title-and-header-django-admin-interface-a6ad6e470d92
# https://www.dothedev.com/blog/django-admin-change-color/ # for color 
# https://docs.djangoproject.com/en/4.1/howto/overriding-templates/ # overriding templates
admin.site.site_header = 'My Admin' # Django administration
admin.site.site_title = 'My Title'
admin.site.index_title = 'Site Administration' # Site administsration
#admin.site.site_url = "Your Page" # VIEW SITE

router = routers.DefaultRouter()
router.register(r'mybusiness',views.MyBusinessView)
router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'gender', views.GenderViewSet)
router.register(r'businesstype', views.BusinessTypeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'businessstatus', views.BusinessStatusViewSet)
router.register(r'businessuserrole', views.BusinessUserRoleViewSet)
router.register(r'collaboratorstatus', views.CollaboratorStatusViewSet)
router.register(r'businessuser', views.BusinessUserViewSet)
router.register(r'insuranceplan', views.InsurancePlanViewSet)
router.register(r'insuranceprovider', views.InsuranceProviderViewSet)
router.register(r'insuranceplantype', views.InsurancePlanTypeViewSet)
router.register(r'insuranceapplication', views.InsuranceApplicationViewSet)
router.register(r'businessinsurance',views.BusinessInsuranceViewSet)
router.register(r'addresss', views.AddressViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'province_state', views.ProvinceStateViewSet)
router.register(r'addresstype', views.AddressTypeViewSet)
router.register(r'clientaddress', views.ClientAddressViewSet)
router.register(r'phonetype', views.PhoneTypeViewSet)
router.register(r'phone', views.PhoneViewSet)
router.register(r'emailtype', views.EmailTypeViewSet)
router.register(r'email',views.EmailViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'medical', views.MedicalViewSet)
router.register(r'document', views.DocumentViewSet)
router.register(r'collaboratorposition', views.CollaboratorPositionViewSet)
router.register(r'complianceentity', views.ComplianceEntityViewSet)
router.register(r'businesscompliance', views.BusinessComplianceViewSet)
router.register(r'businessdocument', views.BusinessDocumentViewSet)
router.register(r'businessmedical', views.BusinessMedicalViewSet)
router.register(r'businessssupervisor', views.BusinessSupervisorViewSet)
router.register(r'businessapproval', views.BusinessApprovalViewSet, basename='businessapproval')
router.register(r'newbusiness', views.NewBusinessViewSet, basename='newbusiness') # for POSTING new business 
router.register(r'files', views.FileViewSet, basename='files') #
router.register(r'editbusiness', views.EditBusinessViewSet, basename='editbusiness') # for PUTTING new business
router.register(r'notification', views.NotificationViewSet, basename='notification')
router.register(r'usernotification', views.UserNotificationViewSet, basename='usernotification')
router.register(r'businessdeclined', views.BusinessDeclinedViewSet, basename='businessdeclined')
router.register(r'player', views.PlayerViewSet, basename='player')
router.register(r'team', views.TeamViewSet, basename='team')

urlpatterns = [
    path('', include("users.urls")),
    path('admin/', admin.site.urls ),
    path('tasks/', include("tasks.urls")),
    path('hello/', include("hello.urls")),
    path('newyear/', include("newyear.urls")),
    #path('flights/', include("flights.urls")), # Don't want to migrate flights
    #path('users/', include("users.urls")), # Root path already using users.urls
    #path('business/',include("business.urls") ), # Replaced by mybusiness
    path('mybusiness/', include("mybusiness.urls")), # To replace business
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += [
    path('file/', include('myapi.urls')),
]

# Media Files in Development Mode:
# https://testdriven.io/blog/django-static-files/#:~:text=Unfortunately%2C%20the%20Django%20development%20server,in%20your%20project%2Dlevel%20URLs.
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


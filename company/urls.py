from rest_framework.routers import DefaultRouter
from company.apps import CompanyConfig
from company.views import CompanyViewSet, ContactViewSet, ProductViewSet

app_name = CompanyConfig.name

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [

] + router.urls

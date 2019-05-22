from rest_framework import routers

from products.views import ProductView

router = routers.DefaultRouter()

router.register('product', ProductView)

urlpatterns = router.urls

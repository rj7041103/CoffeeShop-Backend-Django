from rest_framework import routers
from .api import ProductsViewSet, ReviewsViewSet, ReturnsViewSet, PaymentsViewSet, SubscriptionsViewSet, UsersViewSet

router = routers.DefaultRouter()

router.register('api/v1/products', ProductsViewSet,'products')
router.register('api/v1/users', UsersViewSet,'users')
router.register('api/v1/subscriptions', SubscriptionsViewSet,'subscriptions')
router.register('api/v1/reviews', ReviewsViewSet,'reviews')
router.register('api/v1/returns', ReturnsViewSet,'returns')
router.register('api/v1/payments', PaymentsViewSet,'payments')
router.register('api/v1/inventory', PaymentsViewSet,'inventory')

urlpatterns = router.urls
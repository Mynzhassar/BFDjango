from midterm.core.view_sets import BooksViewSet, JournalsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books', BooksViewSet)
router.register(r'journals', JournalsViewSet)

urlpatterns = router.urls

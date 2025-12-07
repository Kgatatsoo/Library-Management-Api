from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowerViewSet, BorrowRecordViewSet


router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'borrowers', BorrowerViewSet, basename='borrower')
router.register(r'borrow-records', BorrowRecordViewSet, basename='borrowrecord')


urlpatterns = [
    path('', include(router.urls)),
]

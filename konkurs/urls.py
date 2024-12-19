from django.urls import path
from .views import CompetitionViewSet, CategoryViewSet

urlpatterns = [
    # category
    path('get_categories/', CategoryViewSet.as_view({'get': 'get'}), name='get_categories'),
    path('create_category/', CategoryViewSet.as_view({'post': 'create'}), name='create_category'),
    path('update_category/<int:pk>/', CategoryViewSet.as_view({'patch': 'update'}), name='update_category'),
    path('delete_category/<int:pk>/', CategoryViewSet.as_view({'delete': 'delete'}), name='delete_category'),
    # competition
    path('get_competitions/', CompetitionViewSet.as_view({'get': 'get'}), name='get_competitions'),
    path('create_competition/', CompetitionViewSet.as_view({'post': 'create'}), name='create_competition'),
    path('update_competition/<int:pk>/', CompetitionViewSet.as_view({'patch': 'update'}), name='update_competition'),
    path('delete_competition/<int:pk>/', CompetitionViewSet.as_view({'delete': 'delete'}), name='delete_competition'),
]

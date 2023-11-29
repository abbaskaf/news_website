from django.urls import path
from .import views
from .views import SharePost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('',views.list_view,name='home'),
path('newest-posts/', views.NewestPostViews.as_view(), name = 'newest-posts'),
path('<int:year>/<int:month>/<int:day>/<str:slug>/',views.detail_view, name='detail'),
path('category/<slug:category_slug>/', views.CategoryListView.as_view(), name='category_list'),
path('share/<int:pk>', SharePost.as_view(), name="share-post"),
 ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
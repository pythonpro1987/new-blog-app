from django.urls import path
from .views import Bloglistview, Blogdetailview, Blogcreateview, Blogupdateview, Blogdeleteview

urlpatterns = [
    path('', Bloglistview.as_view(), name='home'),
    path('post/<int:pk>/', Blogdetailview.as_view(), name='post_detail'),
    path('post/new/', Blogcreateview.as_view(), name='post_new'),
    path('post/<int:pk>/edit', Blogupdateview.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', Blogdeleteview.as_view(), name='post_delete'),
]

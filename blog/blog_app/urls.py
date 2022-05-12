from django.urls import path
# from . import views
from .views import AddCommentView, DeletePostView, HomeView, ArticlesDetailView,AddPostView, UpdatePostView,AddCategoryView,CategoryView,CategoryListView,LikeView

urlpatterns = [
    # path('',views.home,name="home"),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticlesDetailView.as_view(),name='article-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:catgs>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
]

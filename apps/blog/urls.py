from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogCreateView, CommentCreateView, CommentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(
    r"categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = router.urls

urlpatterns += [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("comment/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/", CommentListView.as_view(), name="comment_list"),
]

from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer, PostSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        return Response(PostSerializer(blog).data)


class BlogCreateView(CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentListView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (ReadOnly,)

    def get(self, requests):
        comments = Comment.objects.all()
        return Response(CommentSerializer(comments, many=True).data)

from django.shortcuts import render
from .models import  Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from rest_framework.views import APIView, Response
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# Create your views here.

################################# API for Getting All Comments starts ##############################

class CommentSerializer(serializers.ModelSerializer):
    sub_comments_list = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ("user", "comment_body","is_sub_comment" , "parent_id", "id", "sub_comments_list")

    def get_sub_comments_list(self, instance):
        sub_comments = Comment.objects.filter(parent_id=instance.id)
        l = []
        for sub_comment in sub_comments:
            d = {}
            d["user"] = sub_comment.user
            d["comment_body"] = sub_comment.comment_body
            d["parent_id"] = sub_comment.parent_id
            d["id"] = sub_comment.id
            l.append(d)
        return l


class CommentsAPI(APIView):
    serializer_class = CommentSerializer

    def get(self, request, format=None):
        comments = Comment.objects.filter(is_sub_comment=False)
        sub_comments_dict = {}
        for comment in comments:
            sub_comments_dict[comment.id] = Comment.objects.filter(parent_id=comment.id)
        serializer = CommentSerializer(comments, many=True)
        # serializer.sub_comments_dict = sub_comments_dict

        return Response(serializer.data)

################################# API for Getting All Comments ends ##############################


################################# API for Adding a Comment starts ##############################

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ( "comment_body","is_sub_comment" , "parent_id", "id")

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class AddCommentAPI(APIView):
    serializer_class = AddCommentSerializer
    permission_class = (AllowAny,)
    
    def post(self, request, format=None):
        data = request.data
        serializer = AddCommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

################################# API for Adding a Comment ends ##############################


################################# API for Editing a Comment starts ##############################

class EditCommentSerializer(serializers.ModelSerializer):
    comment_id = serializers.CharField()
    message = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ( "comment_id", "comment_body", "message")


class EditCommentAPI(APIView):
    serializer_class = EditCommentSerializer
    permission_class = (AllowAny,)
    
    def post(self, request, format=None):
        data = request.data
        comment_id = int(request.POST.get("comment_id"))
        comment_body = request.POST.get("comment_body")
        try:
            comment = Comment.objects.get(pk=comment_id)
            print(comment)
            serializer = EditCommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):            
                serializer.validated_data["comment_id"] = comment_id
                serializer.validated_data["message"] = "Comment Edited"
                comment.comment_body = comment_body
                comment.save()
                return Response(serializer.data)
        except:
            serializer = DeleteCommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):            
                serializer.validated_data["comment_id"] = comment_id
                serializer.validated_data["message"] = "This comment does not exists"
                return Response(serializer.data)

################################# API for Editing a comment ends ##############################


################################# API for Deleting a Comment starts ##############################

class DeleteCommentSerializer(serializers.ModelSerializer):
    comment_id = serializers.CharField()
    message = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ( "comment_id", "message")


class DeleteCommentAPI(APIView):
    serializer_class = DeleteCommentSerializer
    permission_class = (AllowAny,)
    
    def post(self, request, format=None):
        data = request.data
        comment_id = int(request.POST.get("comment_id"))
        try:
            comment = Comment.objects.get(pk=comment_id)
            print(comment)
            serializer = DeleteCommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):            
                serializer.validated_data["comment_id"] = comment_id
                serializer.validated_data["message"] = "Comment Deleted"
                sub_comments = Comment.objects.filter(parent_id=comment.id)
                for sub_comment in sub_comments:
                    sub_comments.delete()
                comment.delete()
                return Response(serializer.data)
        except:
            serializer = DeleteCommentSerializer(data=data)
            if serializer.is_valid(raise_exception=True):            
                serializer.validated_data["comment_id"] = comment_id
                serializer.validated_data["message"] = "This comment does not exists"
                return Response(serializer.data)

################################# API for Deleting a Comment ends ##############################





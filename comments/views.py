from rest_framework.response import Response
from .serializers import CommentSerializer
from rest_framework import status
from rest_framework.views import APIView
from posts.models import Post
from .models import Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


class CommentView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['author'] = user.id
            serializer = CommentSerializer(data=data)
            if not serializer.is_valid():
                return Response({'data':{},
                                 'message': 'something went wrong',
                                 'error':serializer.errors
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            
            return Response({'data':serializer.data,
                                 'message': 'comment is uploaded successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
            
        
        except Exception as ex:
            return Response({
                "message": "An error occurred while commenting the post",
                "data": {},
                "error": str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CommentListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self,request):
        try:
            post_id = request.data['post_id']
            post=Post.objects.filter(id=post_id).first()
            if not post:
                return Response({'data':'',
                                 'message': 'something went wrong',
                                 'error':'Post not found'
                                 },status=status.HTTP_200_OK)
            
            
            comment = Comment.objects.filter(post=post)
            serializer = CommentSerializer(comment,many=True)
            
            per_page = 5
            page_number = request.data.get('page',1)
            
            paginator = Paginator(serializer.data,per_page)
            
            try:
                comment_page = paginator.page(page_number)
            except PageNotAnInteger:
                return Response({'data':'',
                                 'message': 'something went wrong',
                                 'error':'Inavalid page number'
                                 },status=status.HTTP_200_OK)
                
            except EmptyPage:
                response = {
                    "selected_page": page_number,
                    "records_per_page":per_page,
                    "posts":[]
                }
                return Response({'data':response,
                                 'message': 'post is uploaded successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
                
            
            comment_list = comment_page.object_list
            response = {
                    "selected_page": page_number,
                    "records_per_page":per_page,
                    "posts":comment_list
            }
            
            return Response({'data':response,
                                 'message': 'post is uploaded successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
        
        except Exception as ex:
            return Response({
                "message": "An error occurred while fetching the list of posts",
                "data": {},
                "error": str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

from rest_framework.response import Response
from .serializers import PostSerializer,PostListSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


class PostView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        try:
            user = request.user
            post=Post.objects.filter(author=user)
            serializer = PostListSerializer(post,many=True)
            
            per_page = 5
            page_number = int(request.GET.get('page',1))
            
            paginator = Paginator(serializer.data,per_page)
            
            try:
                post_page = paginator.page(page_number)
            except PageNotAnInteger:
                return Response({'data':'',
                                 'message': '',
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
                
            
            post_list = post_page.object_list
            response = {
                    "selected_page": page_number,
                    "records_per_page":per_page,
                    "posts":post_list
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
    
    
    
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['author'] = user.id
            serializer = PostSerializer(data=data)
            if not serializer.is_valid():
                return Response({'data':{},
                                 'message': 'something went wrong',
                                 'error':serializer.errors
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            
            return Response({'data':serializer.data,
                                 'message': 'post is uploaded successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
            
        
        except Exception as ex:
            return Response({
                "message": "An error occurred while posting the blog",
                "data": {},
                "error": str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            
class PostList(APIView):
    
    def get(self,request):
        try:
            post=Post.objects.all()
            serializer = PostListSerializer(post,many=True)
            
            per_page = 5
            page_number = int(request.GET.get('page',1))
            
            paginator = Paginator(serializer.data,per_page)
            
            try:
                post_page = paginator.page(page_number)
            except PageNotAnInteger:
                return Response({'data':'',
                                 'message': '',
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
                
            
            post_list = post_page.object_list
            response = {
                    "selected_page": page_number,
                    "records_per_page":per_page,
                    "posts":post_list
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
            
            
class UpdatePost(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def patch(self, request):
        
        try:
            user = request.user
            data = request.data
            post_id = data['post_id']
            post = Post.objects.get(id=post_id,author=user)
            if not post:
                return Response({'data':{},
                                 'message': 'Post not found',
                                 'error':''
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            serializer = PostSerializer(instance=post,data=data,partial=True)
            
            if not serializer.is_valid():
                return Response({'data':{},
                                 'message': 'something went wrong',
                                 'error':serializer.errors
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            
            return Response({'data':serializer.data,
                                 'message': 'post updated successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
                   
        except Exception as ex:
            return Response({
                "message": "An error occurred while updating the post",
                "data": {},
                "error": str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            

class DeletePost(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self,request):
        try:
            id = request.GET.get('id')
            user = request.user
            post = Post.objects.filter(id=id,author=user).first()
            if not post:
                return Response({'data':{},
                                 'message': 'Post not found',
                                 'error':''
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            post.delete()
            
            return Response({'data':{},
                                 'message': 'post deleted successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_200_OK)
            
            
        except Exception as ex:
            return Response({
                "message": "An error occurred while updating the post",
                "data": {},
                "error": str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
        
        
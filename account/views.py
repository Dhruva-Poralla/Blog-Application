from rest_framework.response import Response
from .serializers import RegisterUserSerializer,LoginSerializer
from rest_framework import status
from rest_framework.views import APIView


class RegisterUserView(APIView):
    
    def post(self,request):
        try:
            
            data = request.data 
            
            serializer = RegisterUserSerializer(data=data)
            if not serializer.is_valid():
                return Response({'data':{},
                                 'message': 'something went wrong',
                                 'error':serializer.errors
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            
            serializer.save()
            
            return Response({'data':'',
                                 'message': 'your account is created successfully',
                                 'error':''
                                 
                                 },status=status.HTTP_201_CREATED)
            
        
        except Exception as ex:
            
            return Response({
                'data': {},
                'message':'Error in registration',
                'error':str(ex)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class Login(APIView):
    
    def post(self, request):
        try:
            data = request.data
            
            serializer = LoginSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({'data':{},
                                 'message': 'something went wrong',
                                 'error':serializer.errors
                                 
                                 },status=status.HTTP_400_BAD_REQUEST)
                
            response = serializer.get_jwt_token(serializer.data)
            
            return Response(response,status=status.HTTP_200_OK)
            
        
        except Exception as ex:
            
            return Response({
                    'data': {},
                    'message':'Error in registration',
                    'error':str(ex)
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

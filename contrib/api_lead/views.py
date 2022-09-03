from socket import IP_DROP_MEMBERSHIP
from django.shortcuts import render
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import viewsets, views, status, generics, mixins

from .serializers import UserSerializer, ItemSerializer
from .models import Item
import time

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#first way
# class ItemListApiView(views.APIView):

#     def get(self, request):
#         item = Item.objects.all()
#         serializer = ItemSerializer(item, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#second way
class ItemListApiView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        # time.sleep(3)
        # import ipdb; ipdb.set_trace()
        return super().list(request, *args, **kwargs)


# first way
# class ItemDetailsApiView(views.APIView):
#     def get(self, request, pk):
#         item = Item.objects.get(pk=pk)
#         serializer = ItemSerializer(item, many=False)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         item = Item.objects.get(pk=pk)
#         item.delete()
#         return Response(status=status.HTTP_200_OK)


#second way
class ItemDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_update(self, serializer):
        print('============= It happened here ===============')
        return super().perform_update(serializer)


#third way
# class ItemDetailsApiView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


def api(request):
    return render(request, 'api.html')
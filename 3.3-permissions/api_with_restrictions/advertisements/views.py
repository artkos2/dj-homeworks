from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def post(self, request):
        Advertisement.objects.create(title=request.data['title'], description=request.data['description'])
        return Response({'Response': 'Добавлено'})

    # def patch(self, request, pk):
    #     Advertisement.objects.filter(id=pk).update(description=request.data['description'])
    #     return Response({'Response': 'Изменено'})

    # def delete(self, pk):
    #     Advertisement.objects.get(id=pk).delete()
    #     return Response({'Response': 'Удалено'})

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return [] 

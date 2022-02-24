from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Brand, Sneaker
from .serializers import SneakerSerializer, BrandSerializer


class FeaturedSneakers(APIView):
    def get(self, request, format=None):
        sneakers = Sneaker.objects.all()[0:5]
        serializer = SneakerSerializer(sneakers, many=True)
        return Response(serializer.data)


class SneakerInfo(APIView):
    def get_object(self, brand_slug, sneaker_slug):
        try:
            return Sneaker.objects.filter(brand__slug=brand_slug).get(slug=sneaker_slug)
        except:
            Sneaker.DoesNotExist
            raise Http404

    def get(self, request, brand_slug, sneaker_slug, format=None):
        sneaker = self.get_object(brand_slug, sneaker_slug)
        serializer = SneakerSerializer(sneaker)
        return Response(serializer.data)


class BrandInfo(APIView):
    def get_object(self, brand_slug):
        try:
            return Brand.objects.get(slug=brand_slug)
        except Sneaker.DoesNotExist:
            raise Http404

    def get(self, request, brand_slug, format=None):
        brand = self.get_object(brand_slug)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        sneakers = Sneaker.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = SneakerSerializer(sneakers, many=True)
        return Response(serializer.data)
    else:
        return Response({"sneakers": []})

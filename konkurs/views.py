from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    CompetitionSerializer,
    CategorySerializer,
)
from .models import (
    Competition,
    Category,
)


class CategoryViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all categories",
        operation_summary="Get all categories",
        responses={
            200: CategorySerializer(),
        },
        tags=['competition']
    )
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create Category",
        operation_summary="Create Category",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='category name'),
            },
            required=['name', ]
        ),
        responses={200:  CategorySerializer()},
        tags=['competition'],
    )
    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Update Category",
        operation_summary="Update Category",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='category name'),
            },
            required=[]
        ),
        responses={200: CategorySerializer()},
        tags=['competition'],
    )
    def update(self, request, *args, **kwargs):
        competition = Category.objects.filter(id=kwargs['pk']).first()
        if competition is None:
            return Response(data={'error': 'Competition not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(competition, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(data={'updated': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete Category",
        operation_description="Delete Category",
        responses={200: 'Successfully deleted'},
        tags=['competition'],
    )
    def delete(self, request, *args, **kwargs):
        competition = Category.objects.filter(id=kwargs['pk']).first()

        if competition is None:
            return Response(data={'error': 'Competition not found'}, status=status.HTTP_404_NOT_FOUND)

        competition.delete()

        return Response(data={'message': 'Successfully deleted'}, status=status.HTTP_200_OK)


class CompetitionViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all competitions",
        operation_summary="Get all competitions",
        responses={
            200: CompetitionSerializer(),
        },
        tags=['competition']
    )
    def get(self, request, *args, **kwargs):
        competition = Competition.objects.all()
        serializer = CompetitionSerializer(competition, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create Competition",
        operation_summary="Create Competition",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='competition name'),
                'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='category id'),
                'description': openapi.Schema(type=openapi.TYPE_INTEGER, description='description'),
                'start_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description='start date in ISO 8601 format (e.g., 2023-11-01T12:00:00Z)'
                ),
                'end_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description='end date in ISO 8601 format (e.g., 2023-11-01T12:00:00Z)'
                ),
                'min_age': openapi.Schema(type=openapi.TYPE_INTEGER, description='min_age'),
                'max_age': openapi.Schema(type=openapi.TYPE_INTEGER, description='max_age'),
                'min_point': openapi.Schema(type=openapi.TYPE_INTEGER, description='min point'),
                'max_point': openapi.Schema(type=openapi.TYPE_INTEGER, description='max point'),
                'image': openapi.Schema(type=openapi.TYPE_FILE, description='image'),
            },
            required=['name', 'category', 'description', 'start_date', 'end_date', 'min_age',
                      'max_age', 'min_point', 'max_point', 'image']
        ),
        responses={200: CompetitionSerializer()},
        tags=['competition'],
    )
    def create(self, request, *args, **kwargs):
        serializer = CompetitionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Update Competition",
        operation_summary="Update Competition",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='competition name'),
                'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='category id'),
                'description': openapi.Schema(type=openapi.TYPE_INTEGER, description='description'),
                'start_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description='start date in ISO 8601 format (e.g., 2023-11-01T12:00:00Z)'
                ),
                'end_date': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_DATETIME,
                    description='end date in ISO 8601 format (e.g., 2023-11-01T12:00:00Z)'
                ),
                'min_age': openapi.Schema(type=openapi.TYPE_INTEGER, description='min_age'),
                'max_age': openapi.Schema(type=openapi.TYPE_INTEGER, description='max_age'),
                'min_point': openapi.Schema(type=openapi.TYPE_INTEGER, description='min point'),
                'max_point': openapi.Schema(type=openapi.TYPE_INTEGER, description='max point'),
                'image': openapi.Schema(type=openapi.TYPE_FILE, description='image'),
            },
            required=[]
        ),
        responses={200: CompetitionSerializer()},
        tags=['competition'],
    )
    def update(self, request, *args, **kwargs):
        competition = Competition.objects.filter(id=kwargs['pk']).first()
        if competition is None:
            return Response(data={'error': 'Competition not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompetitionSerializer(competition, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(data={'updated': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete Competition",
        operation_description="Delete Competition",
        responses={200: 'Successfully deleted'},
        tags=['competition'],
    )
    def delete(self, request, *args, **kwargs):
        competition = Competition.objects.filter(id=kwargs['pk']).first()

        if competition is None:
            return Response(data={'error': 'Competition not found'}, status=status.HTTP_404_NOT_FOUND)

        competition.delete()

        return Response(data={'message': 'Successfully deleted'}, status=status.HTTP_200_OK)

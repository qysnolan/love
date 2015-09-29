from photo.models import Photo
from menu.models import Menu
from .serializers import PhotoSerializer, MenuSerializer
from rest_framework import mixins, viewsets
from .filters import PhotoFilter, MenuFilter


class PhotoViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.none()

    serializer_class = PhotoSerializer
    search_fields = ('title', 'decription', )
    filter_class = PhotoFilter

    def get_queryset(self):
        photos = Photo.objects.all().filter(isActive=True)

        return photos.order_by('photo_id', 'title')

    def filter_queryset(self, queryset):
        queryset = super(PhotoViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if 'ordering' in params:
            column = params['ordering']
            if column == 'title':
                queryset = queryset.order_by('title', 'photo_id')
            if column == '-title':
                queryset = queryset.order_by('-title', 'photo_id')
            if column == 'last_update':
                queryset = queryset.order_by('last_update')
            if column == '-last_update':
                queryset = queryset.order_by('-last_update')

        return queryset


class MenuViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.none()

    serializer_class = MenuSerializer
    search_fields = ('title', 'decription', 'recipe')
    filter_class = MenuFilter

    def get_queryset(self):
        starters = Menu.objects.all().filter(isActive=True)

        return starters.order_by('menu_id', 'title')

    def filter_queryset(self, queryset):
        queryset = super(MenuViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if 'ordering' in params:
            column = params['ordering']
            if column == 'title':
                queryset = queryset.order_by('title', 'menu_id')
            if column == '-title':
                queryset = queryset.order_by('-title', 'menu_id')
            if column == 'last_update':
                queryset = queryset.order_by('last_update')
            if column == '-last_update':
                queryset = queryset.order_by('-last_update')

        return queryset
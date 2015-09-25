from photo.models import Photo
from .serializers import PhotoSerializer
from rest_framework import mixins, viewsets
from .filters import PhotoFilter


class PhotoViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.none()

    serializer_class = PhotoSerializer
    search_fields = ('title', 'decription', )
    filter_class = PhotoFilter

    def get_queryset(self):
        photos = Photo.objects.all()

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
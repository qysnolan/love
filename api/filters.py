from photo.models import Photo
import django_filters


class PhotoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Photo
        fields = ['title', 'description', ]

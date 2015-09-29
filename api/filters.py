from photo.models import Photo
from menu.models import Menu
import django_filters


class PhotoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Photo
        fields = ['title', 'description', ]


class MenuFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')
    type = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Menu
        fields = ['title', 'description', 'type', ]
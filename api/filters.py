from photo.models import Photo
from menu.models import Menu
from wedding.models import Comment
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


class CommentFilter(django_filters.FilterSet):
    person_name = django_filters.CharFilter(lookup_type='icontains')
    comment = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Comment
        fields = ['person_name', 'comment', ]
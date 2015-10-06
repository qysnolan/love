from rest_framework import serializers
from photo.models import Photo
from menu.models import Menu
from wedding.models import Comment


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo

        fields = ('url', 'photo_id', 'title', 'description', 'path',
                  'last_update')


class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu

        fields = ('url', 'menu_id', 'title', 'type', 'description', 'recipe',
                  'photo', 'last_update')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment

        fields = ('url', 'comment_id', 'person_name', 'comment', 'last_update')
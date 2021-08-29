from index.models import Page, Content, Video, Audio, Text
from rest_framework import serializers

class PageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="page-detail", lookup_field='id')
    class Meta:
        model = Page
        fields = ['url']


class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'view_counter', 'data_file', 'subtitles_file']

class AudioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['title', 'view_counter', 'data_file', 'bitrate']

class TextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['title', 'view_counter', 'data']

class ContentDetailSerializer(serializers.ModelSerializer):
    video = VideoDetailSerializer()
    audio = AudioDetailSerializer()
    text = TextDetailSerializer()
    class Meta:
        model = Content
        fields = ['video', 'audio', 'text']

class PageSerializer(serializers.ModelSerializer):
    content_set = ContentDetailSerializer(many=True)
    class Meta:
        model = Page
        fields = ['title', 'content_set']

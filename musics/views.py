from django.shortcuts import render, get_object_or_404

from musics.models import Music
from musics.models import fun_raw_sql_query, fun_sql_cursor_update, fun_sql_cursor_delete
from musics.serializers import MusicSerializer, MusicSerializerV1

from rest_framework import viewsets, status
from rest_framework.response import Response
# pip install djangorestframework==3.1.3
# from rest_framework.decorators import list_route
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser


# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    # API改用JSON回傳 資料 (預設FORM DATA)
    parser_classes = (JSONParser,)

    @action(detail=False, methods=['get'])
    def test(self, request):
        return Response('test', status=status.HTTP_200_OK)

    # /api/music/raw_sql_query/
    # @list_route(methods=['get'])
    # detail = boolean indicating if the current action is configured for a list or detail view.
    @action(detail=False, methods=['get'])
    def raw_sql_query(self, request):
        song = request.query_params.get('song', None)
        music = fun_raw_sql_query(song=song)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # /api/music/{pk}/sql_cursor_update/
    @action(detail=True, methods=['put'], url_path='music_update')
    def sql_cursor_update(self, request, pk=None):
        song = request.data.get('song', None)
        if song:
            music = fun_sql_cursor_update(song=song, pk=pk)
            return Response(music, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='detail_self')
    # 注意 function名稱不能叫detail(可能因為保留字原因)
    def detail001(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }

        return Response(result, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='music_delete')
    def sql_cursor_delete(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        music = fun_sql_cursor_delete(pk=pk)
        return Response(music, status=status.HTTP_200_OK)

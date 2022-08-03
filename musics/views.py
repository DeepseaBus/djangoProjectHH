from django.shortcuts import render

from musics.models import Music
from musics.models import fun_raw_sql_query, fun_sql_cursor_update
from musics.serializers import MusicSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
# pip install djangorestframework==3.1.3
# from rest_framework.decorators import list_route
from rest_framework.decorators import action


# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    @action(detail=True, methods=['get'])
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
    @action(detail=True,methods=['put'])
    def sql_cursor_update(self, request, pk=None):
        song = request.data.get('song', None)
        if song:
            music = fun_sql_cursor_update(song=song, pk=pk)
            return Response(music, status=status.HTTP_200_OK)

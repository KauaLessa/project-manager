from rest_framework import viewsets
from .models import Projetos
from colaboradores.models import Colaboradores
from .serializers import ProjetosSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from colaboradores.serializers import ColaboradoresSerializer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

class ProjetosViewSet(viewsets.ModelViewSet):
    queryset = Projetos.objects.prefetch_related('equipe').all()
    serializer_class = ProjetosSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]  

    @action(detail=True, methods=['post'])
    def inativar(self, request, pk=None):
        projeto = self.get_object()
        projeto.ativo = False
        projeto.save()
        return Response({'status':'inativo'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def equipe(self, request, pk=None):
        projeto = self.get_object()
        colaboradores = Colaboradores.objects.filter(equipe__projeto=projeto)
        serializer = ColaboradoresSerializer(colaboradores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'])
    def atualizar_equipe(self, request, pk=None):
        projeto = self.get_object()

        try:
            equipe_atualizada = request.data['equipe']
        except KeyError as e:
            return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(equipe_atualizada, list):
            error = {'equipe':'Equipe deve ser uma lista'}
            response_status = status.HTTP_400_BAD_REQUEST
            return Response(error, status=response_status)
        
        try:
            projeto.equipe.set(equipe_atualizada)
            projeto.qtd_membros = projeto.equipe.count()
            projeto.save(update_fields=['qtd_membros'])
            serializer = ProjetosSerializer(projeto)
            equipe = serializer.data['equipe']
            return Response({'equipe_atualizada':equipe}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
class ProjetosForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cadastrar_projeto.html'

    def get(self, request, *args, **kwargs):
        serializer = ProjetosSerializer()
        return Response({'serializer':serializer})
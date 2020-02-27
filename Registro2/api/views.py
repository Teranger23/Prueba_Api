from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Serie
from api.serializers import SerieSerializer

class JSONResponse(HttpResponse):
    """
    Un HttpResponse que renderiza su contenido en formato JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs) 

@csrf_exempt
def serie_list(request):
    """   
    Lista todas las series, o crea una nueva serie   
    """
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':           
        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse({'Mensaje': 'No Se pudo Registrar'}, status=400)


def serie_detail(request, pk):
    """
    Recuperar, actualizar o eliminar una serie.
    """
    try:
        serie = Serie.objects.get(pk=pk)
    except Serie.DoesNotExist:
        return JSONResponse({'Mensaje': 'La Serie No Existe'}, status=400)

    if request.method == 'GET':
        serializer = SerieSerializer(serie)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()          
            return JSONResponse({'Mensaje: ':'Actualizacion Exitosa','data':serializer.data}, status=200)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':          
            serie.delete()
            return JSONResponse({'Mensaje': 'Borrado exitoso'}, status=200)
        
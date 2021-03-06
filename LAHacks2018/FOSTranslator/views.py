from django.shortcuts import render

# import os
# os.environ['DJANGO_SETTINGS_MODULE']='LAHacks2018.settings'

import os
from string import punctuation

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'LAHacks2018.settings'
application = get_wsgi_application()

import json

from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from FOSTranslator.models import Idiom, InputText
from FOSTranslator.serializers import FOSTranslatorSerializer

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
#@csrf_exempt
'''
class IdiomViewSet(viewsets.ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = FOSTranslatorSerializer
'''
class InputTextViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InputText.objects.all()
    serializer_class = FOSTranslatorSerializer

@api_view(['GET'])
def get_idioms(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        text_to_check = request.data.text

        idioms = Idiom.objects.all()

        list_of_dict_idioms = []
        text_to_check = ''.join(c for c in text_to_check if c not in punctuation).lower()

        for idiom_instance in idioms:
            #print (idiom_instance.idiom)
            #print (text_to_check)
            idiom_instance.idiom = ''.join(c for c in idiom_instance.idiom if c not in punctuation).lower()
            if idiom_instance.idiom in text_to_check:

                dict2 = {'index': str(text_to_check.find(idiom_instance.idiom)), 'idiom': idiom_instance.idiom, 'literal': idiom_instance.definition}
                list_of_dict_idioms.append(dict2)
        #print (list_of_dict_idioms)

        n_dict = json.dumps(list_of_dict_idioms)
        print(n_dict)
        return n_dict
'''
one = {}
one['text'] = "raining cats and dogs"
two = {}
two['data'] = one
two['method'] = "GET"
x = get_idioms(two)
'''


        # serializer = FOSTranslatorSerializer(FOSTranslator, many=True)
        # return JsonResponse(serializer.data, safe=False)

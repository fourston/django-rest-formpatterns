from django.views import generic
from .models import FormPattern, FormField
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .FormSerializer import FormSerializer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework

# Create your views here.
class FormView(generic.ListView):
    template_name = 'formpatterns/forms.html'
    context_object_name = 'form_list'

    def get_queryset(self):
        return FormPattern.objects.all()

class ProductFilter(django_filters.FilterSet):

    fieldName = django_filters.CharFilter(name="formFields__fieldName")
    class Meta:
        model = FormPattern
        fields = ['fieldName']

class FromListView(generics.ListAPIView):
    queryset = FormPattern.objects.all()
    serializer_class = FormSerializer
    filter_class = ProductFilter


@api_view(['GET', 'POST'])
@parser_classes((JSONParser,))
def form_list(request):

    if request.method == 'GET':
        forms = FormPattern.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            forms = FormPattern.objects.all()
            serializer = FormSerializer(forms, many=True)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


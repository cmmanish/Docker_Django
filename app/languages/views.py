from rest_framework.views import APIView

from .models import Language
from .serializers import LanguageSerializer


# Create your views here.
class LanguageView(APIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

from rest_framework import viewsets

from .models import Ruleset
from .serializers import RulesetSerializer


class RulesetViewSet(viewsets.ModelViewSet):
    queryset = Ruleset.objects.all()
    serializer_class = RulesetSerializer

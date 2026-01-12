from rest_framework import serializers

from .models import Snapshot


class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = "__all__"

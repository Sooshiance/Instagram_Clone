from rest_framework import serializers

from .models import Explorer


class ExplorerSerializers(serializers.ModelSerializer[Explorer]):
    class Meta:
        model = Explorer
        fields = [
            "pk",
            "eid",
            "post",
            "all_data",
            "first_day_data",
            "created_at",
        ]

from rest_framework import serializers

from ads.models import Selection
from ads.serializers.ad import AdSerializer


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        exclude = ["items"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = "__all__"
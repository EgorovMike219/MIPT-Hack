from rest_framework import serializers
from .models import Test, Github, Picture


# from datetime import datetime

class githubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Github
        fields = ('id', 'login', 'password')

        def create(self, validated_data):
            return Github.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.Id = validated_data.get('id', instance.Id)
            instance.Login = validated_data.get('login', instance.Login)
            instance.Password = validated_data.get('password', instance.Password)
            instance.save()
            return instance


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'source1', 'source2', 'source3', 'source4', 'source5')

        def create(self, validated_data):
            return Test.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.Id = validated_data.get('id', instance.Id)
            instance.Source1 = validated_data.get('source1', instance.Source1)
            instance.Source2 = validated_data.get('source1', instance.Source1)
            instance.Source3 = validated_data.get('source1', instance.Source1)
            instance.Source4 = validated_data.get('source1', instance.Source1)
            instance.Source5 = validated_data.get('source1', instance.Source1)
            instance.save()
            return instance


class pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'source', 'processed')

        def create(self, validated_data):
            return Picture.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.Id = validated_data.get('id', instance.Id)
            instance.Source = validated_data.get('source', instance.Source)
            instance.Processed = validated_data.get('processed', instance.Processed)
            instance.save()
            return instance
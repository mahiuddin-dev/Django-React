from rest_framework import serializers
from .models import Person,Skills,SocialMedia


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skill',]

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['social_media','link',]

class PersonSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True, read_only=True)
    social_media = SocialMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = ['id','name','title','skills','social_media',]
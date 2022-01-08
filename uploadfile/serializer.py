from django.db import models
from rest_framework import serializers
from .models import Profile,UserProfile

class profileSerializer(serializers.ModelSerializer):
    
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Profile
        fields = ('name', 'image','image_url')

    def get_image_url(self, obj):
        return obj.image.url
    
    # class Meta:
    #     model = Profile
    #     fields = "__all__"
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}
        
        
        
    
    
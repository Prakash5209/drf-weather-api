from django.contrib.auth.models import User
from rest_framework import serializers



class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password',)
        extra_kwargs = {'password':{'write_only':True}}


    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    password = serializers.CharField()


    #react ma garnu paryo aba 

    #const [data,setData]=useState({});

    #install axios

    #const response =axios.get("url");

    #if(respose){
    #    setData(response.data)
    #}

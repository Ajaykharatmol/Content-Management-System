from ContentManagementSystemAPIs.models import RegisterUser, Task
from rest_framework import serializers
import re
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    Full_Name = serializers.CharField(label='Full_Name')


    Email = serializers.EmailField(label='Email Address')
    Phone = serializers.CharField(label='Phone')

    Password = serializers.CharField(label='Password')
    Password2 = serializers.CharField(label='Confirm Password')


    def validate_password2(self, value):
        data = self.get_initial()
        Password1 = data.get("password")
        Password2 = value
        if Password1 != Password2:
            raise serializers.ValidationError("Password Must Match")

        """Validates that a password is as least 8 characters long and has at least
            2 digits and 1 Upper case letter.
            """
        msg = 'Note: password is at least 8 characters long and has at least 2 digits and 1 Upper case letter'
        min_length = 8

        if len(value) < min_length:
            raise serializers.ValidationError('Password must be at least {0} characters '
                                              'long.'.format(min_length) + msg)

        # check for 2 digits
        if sum(c.isdigit() for c in value) < 2:
            raise serializers.ValidationError('Password must container at least 2 digits.' + msg)

        # check for uppercase letter
        if not any(c.isupper() for c in value):
            raise serializers.ValidationError('Password must container at least 1 uppercase letter.' + msg)

        return value

    def validate_email(self, value):
        data = self.get_initial()
        Email = data.get("Email")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, Email)):
            username_qs = User.objects.filter(username=Email)
            if username_qs.exists():
                raise serializers.ValidationError("Email Id already exists")
            else:
                pass
            return value
        raise serializers.ValidationError("invalid Email id")

    def validate_mob_no(self, value):
        data = self.get_initial()
        Phone = data.get("Phone")
        #regex = '^(\+91[\-\s]?)?[0]?\d{9}$'
        regex = '^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
        if (re.search(regex, Phone)):
            return value
        else:
            raise serializers.ValidationError(
                "Phone number must be entered in the format: '9999999999',9892799999 Up to 10 digits allowed.")

    def create(self, validated_data):

        user = RegisterUser.objects.create(
            Email=validated_data['Email'],
            Full_Name=validated_data['Full_Name'],
            

            Phone=validated_data['Phone'],
            Password=validated_data['Password']
        )
        # user.set_password(validated_data['mob_no'])
        # user.mob_no = validated_data['mob_no']
        #
        # user.save()

        return validated_data

    class Meta:
        model = RegisterUser
        fields = ('id','Full_Name', 'Email', 'Phone', 'Password', 'Password2')



class GelUserDetailsSerializer(serializers.ModelSerializer):
    # profile_image = Base64ImageField(max_length=None, use_url=True, )

    class Meta:
        model = RegisterUser
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.Full_Name = validated_data.get('Full_Name', instance.Full_Name)
       
        instance.Email = validated_data.get('Email', instance.Email)
        instance.Phone = validated_data.get('Phone', instance.Phone)

        

        instance.save()

        return instance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['Title', 'Body', 'Summary', 'Categories']





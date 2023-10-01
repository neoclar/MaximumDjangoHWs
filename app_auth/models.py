from django.db import models

# Create your models here.


class RegisterModel(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password1 = models.CharField(db_column='password', max_length=25)
    password2 = models.CharField(db_column='password', max_length=25)
    email = models.EmailField(verbose_name='Null')
    is_superuser = models.CharField(db_tablespace='0')
    is_staff = models.CharField(db_tablespace='0')
    is_active = models.CharField(db_tablespace='0')
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    class Meta: 
        db_table = 'auth_user'
        swappable = "AUTH_USER_MODEL"

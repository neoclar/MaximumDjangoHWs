from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# ОБЪЯВЛЕНИЯ:
# -------------------
# Поля модели:
# 1. Заголовок
# 2. Описание
# 3. Дата создания
# 4. Цена
# 5. Уместность торга (булевое поле)
# -------------------

User = get_user_model()

class Advertisement(models.Model):
    # Поля:
    title = models.CharField('Заголовок', max_length=25)
    description = models.TextField('Описание', max_length=2048)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f'id={self.id}, title={self.title}, price={self.price}'

    class Meta: 
        db_table = 'advertisements'

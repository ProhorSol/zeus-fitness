from django.db import models
from django.utils import timezone

# Create your models here.

class Subscription(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    duration = models.IntegerField('Длительность (месяцев)')
    features = models.TextField('Преимущества')

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'

    def __str__(self):
        return self.name

    def get_features_list(self):
        return self.features.split('\n')

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает оплаты'),
        ('paid', 'Оплачен'),
        ('cancelled', 'Отменен'),
    )

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, verbose_name='Абонемент')
    name = models.CharField('Имя', max_length=100, default='')
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20, default='')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    paid_at = models.DateTimeField('Дата оплаты', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} - {self.subscription.name}'

class Service(models.Model):
    title = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=50, help_text='Название класса иконки Font Awesome')
    is_active = models.BooleanField('Активно', default=True)
    order = models.IntegerField('Порядок', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новое'),
        ('in_progress', 'В обработке'),
        ('answered', 'Отвечено'),
        ('spam', 'Спам'),
    )

    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    message = models.TextField('Сообщение')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    answered_at = models.DateTimeField('Дата ответа', null=True, blank=True)
    admin_notes = models.TextField('Заметки администратора', blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f'Сообщение от {self.name} ({self.created_at.strftime("%d.%m.%Y %H:%M")})'

class Gallery(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='gallery/')
    description = models.TextField('Описание', blank=True)
    category = models.CharField('Категория', max_length=100, choices=[
        ('gym', 'Тренажерный зал'),
        ('yoga', 'Йога'),
        ('cardio', 'Кардио'),
        ('group', 'Групповые занятия')
    ])
    is_active = models.BooleanField('Активно', default=True)
    order = models.IntegerField('Порядок', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Галерея'
        ordering = ['order']

    def __str__(self):
        return self.title

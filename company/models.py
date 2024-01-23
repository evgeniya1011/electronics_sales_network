from django.db import models


NULLABLE = {'blank': True, 'null': True}
SUBJECT_CHOICES = (
    ('0', 'Factory'),
    ('1', 'Retail'),
    ('2', 'Individual entrepreneur')
)


class Contacts(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица',
                              **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома',
                                    **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Company(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    subjects_electronic_network = models.CharField(max_length=50,
                                                   choices=SUBJECT_CHOICES,
                                                   verbose_name='Субъект торговой сети')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE,
                                 verbose_name='Контакты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=19, decimal_places=2,
                               verbose_name='Задолженность перед поставщиком')
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=20, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата реализации')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Продавец',
                                related_name='products')

    def __str__(self):
        return f'{self.title} - модель {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

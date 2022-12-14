from django.db import models


class Search(models.Model):
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.url


class DadosSensiveis(models.Model):
    TIPO_VULNERABILIDADE = (
        ('1', 'DADOS SENSIVEIS'),
        ('2', 'XSS'),
        ('3', 'SQL INJECTOR'),
        ('4', 'FILES')
        )
    search_date = models.DateField(auto_now=True)
    link = models.CharField(max_length=500)
    tipo_vulnerabilidade = models.CharField(
        'Vulnerabilidade',
        max_length=20,
        choices=TIPO_VULNERABILIDADE)
    url_primary_id = models.ForeignKey(
        Search,
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        caminho = self.link.split("/")[2]
        hostname = caminho.split('.')[1]
        return hostname

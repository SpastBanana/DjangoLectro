from django.db import models

class teamPerson(models.Model):
    ALIGN_CHOICES = (
        ('left', 'left'),
        ('right', 'right'),
    )
    position = models.CharField(max_length=200, choices=ALIGN_CHOICES, default='left')
    name = models.CharField(max_length=200)
    workFunction = models.CharField(max_length=200)
    text = models.TextField(max_length=340)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Het team"

class portfolioContent(models.Model):
    title = models.CharField(max_length=200)
    projectDate = models.CharField(max_length=200)
    text = models.TextField(max_length=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Portfolio"
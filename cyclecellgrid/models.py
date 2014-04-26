from django.db import models

# Create your models here.

class CreateNewCell(models.Manager):
    def create_cell(self, value="111111111", color="FFFFFF"):
        cell = self.create(value=value, color=color)
        return cell


class CellGrid(models.Model):
    value = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    objects = CreateNewCell()



from django.shortcuts import render
from cyclecellgrid.models import CellGrid
import random

# Create index views
def index(request):
    CellGrid.objects.all().delete()
    colorlist = ()
    for num in range(0,9):
        randomNum = random.randint(100000000,999999999)
        colorcode = 0x00ffffff & randomNum
        cell = CellGrid.objects.create_cell(str(randomNum), str(colorcode))
        cell.save()
    return render(request, "index.html", {"cell": CellGrid.objects.all()})

# Create cyclecell views
def cyclecell(request):
    matrix = []
    for number in CellGrid.objects.all():
        matrix.append(number.value)

    newMatrix = []
    newMatrix.append(matrix[3])
    newMatrix.append(matrix[0])
    newMatrix.append(matrix[1])
    newMatrix.append(matrix[6])
    newMatrix.append(matrix[4])
    newMatrix.append(matrix[2])
    newMatrix.append(matrix[7])
    newMatrix.append(matrix[8])
    newMatrix.append(matrix[5])

    CellGrid.objects.all().delete()

    for num in newMatrix:
        colorcode = colorcode = 0x00ffffff & int(num)
        cell = CellGrid.objects.create_cell(str(num), str(colorcode))
        cell.save()

    return render(request, "index.html", {"cell": CellGrid.objects.all()})

from django.http import HttpResponse


def index(request):
    return HttpResponse("Esto va a ser el inventario!")
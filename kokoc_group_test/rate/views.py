from django.http import JsonResponse

from .models import Valute


def get_rate(request):
    queryset = Valute.objects.all()
    charcode = request.GET.dict().get('charcode')
    date = request.GET.dict().get('date')
    if charcode:
        queryset = queryset.filter(charcode=charcode)
    if date:
        queryset = queryset.filter(date=date)
    return JsonResponse(
        data=list(queryset.values('charcode', 'date', 'rate')),
        safe=False
        )

from django.shortcuts import get_list_or_404, render

from booking.models import Train


def index(request):
    ''' Render index.html '''
    return render(request, 'index.html')


def search_results(request):
    ''' Display search results filter by queries '''
    trains = get_list_or_404(Train.objects.filter(
        date=request.GET.get('date')),
        route__source__name=request.GET.get('source'),
        route__destination__name=request.GET.get('destination'),
    )
    context = {'trains': trains}

    return render(request, 'search.html', context)

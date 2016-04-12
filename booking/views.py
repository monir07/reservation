from django.shortcuts import get_list_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView

from booking.models import Train, Ticket
from booking.forms import TicketForm
from booking.utils import class_name, update_count


def index(request):
    ''' Render index.html '''
    return render(request, 'index.html')


def search_results(request):
    ''' Display search results filter by queries '''
    trains = get_list_or_404(Train.objects.filter(
        date=request.GET.get('date'),
        route__source__name=request.GET.get('source'),
        route__destination__name=request.GET.get('destination'),
    ))
    context = {'trains': trains}
    return render(request, 'search.html', context)


def book_ticket(request):
    ''' Book Tikcet'''
    if request.method == 'GET':
        form = TicketForm()
        train = Train.objects.get(pk=request.GET.get('train'))
        seat_class = request.GET.get('class')
        train_context = {
            'train': train,
            'class_model_name': seat_class,
            'class': class_name(seat_class),
            'seat': getattr(train, seat_class)
        }
    elif request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            train = Train.objects.get(pk=request.POST.get('train'))
            form.instance.train = train
            instance = form.save()
            # update count
            update_count(train, request.POST.get('class'))
            return HttpResponseRedirect(reverse('booking:get_ticket', args=(instance.id,)))
    else:
        return HttpResponseRedirect('/')

    return render(request, 'booking.html', {'form': form, 'train_context': train_context})


class GetTicket(DetailView):
    model = Ticket
    template_name = 'ticket.html'
    context_object_name = 'ticket'

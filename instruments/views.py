from instruments.models import Instrument
from instruments.forms import InstrumentModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

class InstrumentListView(ListView):
    model = Instrument
    template_name = 'instruments.html'
    context_object_name = 'instruments'

    # buscador 
    def get_queryset(self):
        instruments = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            instruments = instruments.filter(Q(product__icontains=search) | Q(category__icontains=search))
        return instruments
    

# detalhes do produto
class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = 'instrument_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch') # autorização das views para acesso à edição e deleção
class NewInstrumentCreateView(CreateView):
    model = Instrument
    form_class = InstrumentModelForm
    template_name = 'new_instrument.html'
    success_url = '/instruments'

    # ir para a página de detalhes do objeto
    def get_success_url(self):
        return reverse_lazy('instrument_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class InstrumentUpdateView(UpdateView):
    model = Instrument
    form_class = InstrumentModelForm
    template_name = 'instrument_update.html'

    # ir para a página de detalhes do objeto
    def get_success_url(self):
        return reverse_lazy('instrument_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class InstrumentDeleteView(DeleteView):
    model= Instrument
    template_name = 'instrument_delete.html'
    success_url = '/instruments/'
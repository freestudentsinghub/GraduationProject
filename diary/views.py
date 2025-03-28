from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.forms import RecordForm
from diary.models import Record


# Create your views here.
class HomeView(TemplateView):
    template_name = "base.html"


class RecordList(ListView):
    model = Record
    template_name = "record_list.html"


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('diary:record_list')

    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('diary:record_list')


class RecordDetailView(DetailView):
    model = Record
    template_name = "record_detail.html"


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('diary:record_list')
    template_name = "record_confirm_delete.html"


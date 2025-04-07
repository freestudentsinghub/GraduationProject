from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.forms import RecordForm
from diary.models import Record


# Create your views here.
class HomeView(TemplateView):
    template_name = "diary/base.html"


class RecordList(ListView):
    model = Record
    template_name = "diary/record_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'diary/record_form.html'
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
    template_name = 'diary/record_form.html'
    success_url = reverse_lazy('diary:record_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class RecordDetailView(DetailView):
    model = Record
    template_name = "diary/record_detail.html"


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('diary:record_list')
    template_name = "diary/record_confirm_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


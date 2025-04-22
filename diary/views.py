from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from diary.forms import RecordForm, DiarySearchForm
from diary.models import Record
from django.db.models import Q


class DairyListMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        records = Record.objects.filter(user=self.request.user)
        context['date_list'] = records.values_list('created_date', flat=True).distinct()
        return context


# Create your views here.
class HomeView(TemplateView):
    template_name = "diary/base.html"


class RecordList(ListView):
    model = Record
    template_name = "diary/record_list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(owner=self.request.user)
        else:
            return Record.objects.none()


class RecordCreateView(LoginRequiredMixin, CreateView):
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


class RecordUpdateView(LoginRequiredMixin, UpdateView):
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


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy('diary:record_list')
    template_name = "diary/record_confirm_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class DiarySearchView(View):
    form_class = DiarySearchForm
    template_name = 'diary/search_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET or None)
        diaries = []

        if request.GET and form.is_valid():
            query = form.cleaned_data['query']
            diaries = Record.objects.filter(Q(name__icontains=query) | Q(note__icontains=query), owner=request.user)

        return render(request, self.template_name, {'form': form, 'object_list': diaries})
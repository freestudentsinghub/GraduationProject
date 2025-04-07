from django.urls import path
from django.views.decorators.cache import cache_page


from diary.views import HomeView, RecordList, RecordCreateView, RecordUpdateView, RecordDetailView, RecordDeleteView, \
    DiarySearchView

app_name = 'diary'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('record/list', RecordList.as_view(), name='record_list'),
    path('record/create', RecordCreateView.as_view(), name='record_create'),
    path('record/update/<int:pk>', RecordUpdateView.as_view(), name='record_update'),
    path('record/<int:pk>', RecordDetailView.as_view(), name='record_detail'),
    path('record/delete/<int:pk>', RecordDeleteView.as_view(), name='record_delete'),
    path('search', DiarySearchView.as_view(), name='diary_search'),
]

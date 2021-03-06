from django.apps import AppConfig
from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


class StoreConfig(OscarConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'Store'
    namespace = 'store'

    def ready(self):
        super().ready()
        self.store_list_view = get_class(
            'Store.views', 'StoreListView')
        self.store_detail_view = get_class(
            'Store.views', 'StoreDetailView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.store_list_view.as_view(), name='index'),
            re_path(r'^view/(?P<pk>\d+)/$',
                    self.store_detail_view.as_view(), name='details'),
        ]
        return self.post_process_urls(urls)

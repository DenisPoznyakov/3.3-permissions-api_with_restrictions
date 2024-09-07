from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["creator", "title", "created_at"]

from nautobot.extras.plugins import PluginFilterSetExtension
from nautobot.utilities.filters import MultiValueCharFilter


def suffix_search(queryset, name, value):
    return queryset.filter(description=f"{value[0]}.nautobot.com")


class TenantFilterSetExtension(PluginFilterSetExtension):
    model = "tenancy.tenant"

    def filterset(self):
        description = MultiValueCharFilter(field_name="description", label="Description")  # Creation of a new filter
        sdescrip = MultiValueCharFilter(
            field_name="description", label="Description", method=suffix_search
        )  # Creation of new filter with custom method
        dtype = MultiValueCharFilter(
            field_name="sites__devices__device_type__slug", label="Device Type"
        )  # Creation of a nested filter
        return {
            "example-plugin-description": description,
            "example-plugin-dtype": dtype,
            "example-plugin-sdescrip": sdescrip,
        }


filter_extensions = [TenantFilterSetExtension]

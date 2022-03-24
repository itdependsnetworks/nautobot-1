from django import forms

from nautobot.extras.plugins import PluginFilterForm


class TenantFilterForms(PluginFilterForm):
    model = "tenancy.tenant"

    def filter_forms(self):
        description = forms.CharField(required=False, label="Description")  # Leveraging a custom filter
        dtype = forms.CharField(required=False, label="Device Type")  # Leveraging a custom and nested filter
        slug__ic = forms.CharField(required=False, label="Slug Contains")  # Leveraging an existing filter
        sdescrip = forms.CharField(
            required=False, label="Suffix Description"
        )  # Leveraging a custom method search filter
        return {
            "example-plugin-description": description,
            "example-plugin-dtype": dtype,
            "slug__ic": slug__ic,
            "example-plugin-sdescrip": sdescrip,
        }


filter_forms = [TenantFilterForms]

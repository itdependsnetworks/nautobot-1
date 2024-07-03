# Generated by Django 4.2.13 on 2024-06-12 04:06

import uuid

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion

import nautobot.core.models.fields
import nautobot.extras.models.mixins
import nautobot.extras.utils


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("cloud", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cloudtype",
            name="content_types",
            field=models.ManyToManyField(
                limit_choices_to=nautobot.extras.utils.FeatureQuery("cloud_types"),
                related_name="cloud_types",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.CreateModel(
            name="CloudService",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("extra_config", models.JSONField(blank=True, null=True)),
                (
                    "cloud_account",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="cloud_services",
                        to="cloud.cloudaccount",
                    ),
                ),
                (
                    "cloud_network",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="cloud_services",
                        to="cloud.cloudnetwork",
                    ),
                ),
                (
                    "cloud_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="cloud_services", to="cloud.cloudtype"
                    ),
                ),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "abstract": False,
                "ordering": ["name"],
            },
            bases=(
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
                models.Model,
            ),
        ),
    ]

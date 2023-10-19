# Generated by Django 3.2.22 on 2023-10-19 20:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SanctionsCheckFailure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('lms_user_id', models.IntegerField(db_index=True, null=True)),
                ('city', models.CharField(default='', max_length=32)),
                ('country', models.CharField(max_length=2)),
                ('sanctions_type', models.CharField(max_length=255)),
                ('system_identifier', models.CharField(max_length=255)),
                ('metadata', models.JSONField()),
                ('sdn_check_response', models.JSONField()),
            ],
            options={
                'verbose_name': 'Sanctions Check Failure',
            },
        ),
        migrations.CreateModel(
            name='SanctionsFallbackMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file_checksum', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('download_timestamp', models.DateTimeField()),
                ('import_timestamp', models.DateTimeField(blank=True, null=True)),
                ('import_state', models.CharField(choices=[('New', 'New'), ('Current', 'Current'), ('Discard', 'Discard')], default='New', max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SanctionsFallbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(db_index=True, default='', max_length=255)),
                ('sdn_type', models.CharField(db_index=True, default='', max_length=255)),
                ('names', models.TextField(default='')),
                ('addresses', models.TextField(default='')),
                ('countries', models.CharField(default='', max_length=255)),
                ('sanctions_fallback_metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanctions.sanctionsfallbackmetadata')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSanctionsFallbackMetadata',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file_checksum', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('download_timestamp', models.DateTimeField()),
                ('import_timestamp', models.DateTimeField(blank=True, null=True)),
                ('import_state', models.CharField(choices=[('New', 'New'), ('Current', 'Current'), ('Discard', 'Discard')], db_index=True, default='New', max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical sanctions fallback metadata',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSanctionsFallbackData',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('source', models.CharField(db_index=True, default='', max_length=255)),
                ('sdn_type', models.CharField(db_index=True, default='', max_length=255)),
                ('names', models.TextField(default='')),
                ('addresses', models.TextField(default='')),
                ('countries', models.CharField(default='', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sanctions_fallback_metadata', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sanctions.sanctionsfallbackmetadata')),
            ],
            options={
                'verbose_name': 'historical sanctions fallback data',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSanctionsCheckFailure',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('lms_user_id', models.IntegerField(db_index=True, null=True)),
                ('city', models.CharField(default='', max_length=32)),
                ('country', models.CharField(max_length=2)),
                ('sanctions_type', models.CharField(max_length=255)),
                ('system_identifier', models.CharField(max_length=255)),
                ('metadata', models.JSONField()),
                ('sdn_check_response', models.JSONField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Sanctions Check Failure',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

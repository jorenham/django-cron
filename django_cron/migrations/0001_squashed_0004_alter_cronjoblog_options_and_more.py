# Generated by Django 5.0.8 on 2024-08-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('django_cron', '0001_initial'), ('django_cron', '0002_remove_max_length_from_CronJobLog_message'), ('django_cron', '0003_cronjoblock'), ('django_cron', '0004_alter_cronjoblog_options_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronJobLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200, unique=True)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CronJobLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_success', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, default='')),
                ('ran_at_time', models.TimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'get_latest_by': 'start_time',
                'indexes': [models.Index(fields=['code', 'start_time'], name='django_cron_code_966ed3_idx'), models.Index(fields=['code', 'start_time', 'ran_at_time'], name='django_cron_code_21f381_idx'), models.Index(fields=['code', 'is_success', 'ran_at_time'], name='django_cron_code_89ad04_idx'), models.Index(fields=['code'], name='django_cron_code_26aea9_idx'), models.Index(fields=['start_time'], name='django_cron_start_t_9e0b8f_idx'), models.Index(fields=['end_time'], name='django_cron_end_tim_c3cfdc_idx'), models.Index(fields=['ran_at_time'], name='django_cron_ran_at__aa3be6_idx')],
            },
        ),
    ]

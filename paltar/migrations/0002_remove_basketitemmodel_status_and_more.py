# Generated by Django 4.2.5 on 2023-10-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paltar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitemmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='basketitemmodel',
            name='d_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('UD', 'Undelivered')], default='UD', max_length=2),
        ),
        migrations.AddField(
            model_name='basketitemmodel',
            name='o_status',
            field=models.CharField(choices=[('B', 'Basket'), ('O', 'Order')], default='B', max_length=1),
        ),
    ]

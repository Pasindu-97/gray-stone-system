# Generated by Django 4.2.2 on 2023-10-04 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('address', models.CharField(max_length=1023, verbose_name='Address')),
                ('contact_no', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('completed_projects', models.IntegerField(default=0, verbose_name='Completed Projects')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('contact_no', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('bank_name', models.CharField(max_length=127, verbose_name='Bank Name')),
                ('branch_name', models.CharField(max_length=127, verbose_name='Branch Name')),
                ('bank_acc_num', models.CharField(max_length=127, verbose_name='Account Number')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SupplierOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ordered_quantity', models.IntegerField(verbose_name='Ordered Quantity')),
                ('received_quantity', models.IntegerField(blank=True, null=True, verbose_name='Received Quantity')),
                ('bill_amount', models.IntegerField(verbose_name='Bill Amount')),
                ('paid_amount', models.IntegerField(blank=True, null=True, verbose_name='Paid Amount')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='supplier_order', to='quotations.item', verbose_name='Item')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='order', to='stakeholders.supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Supplier Order',
                'verbose_name_plural': 'Supplier Orders',
                'ordering': ['id'],
            },
        ),
    ]
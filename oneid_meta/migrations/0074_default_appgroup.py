# Generated by Django 2.2.10 on 2020-06-23 12:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


def create_root_app_group(apps, schema_editor):
    AppGroup = apps.get_model('oneid_meta', 'AppGroup')
    AppGroup.objects.create(
        uid='root',
        name='root',
        remark='所有顶级的应用分组的父级，可视为整个公司。请勿修改',
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='APP名称'),
        ),
        migrations.CreateModel(
            name='AppGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('uid', models.CharField(max_length=255, verbose_name='APP分组的唯一标识')),
                ('name', models.CharField(default='', max_length=255, verbose_name='APP分组名称')),
                ('remark', models.TextField(blank=True, default='', verbose_name='APP分组的详细介绍')),
                ('top', models.CharField(blank=True, default='root', max_length=255, verbose_name='范围的顶点uid')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='oneid_meta.AppGroup', verbose_name='父级节点')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(create_root_app_group),

    ]

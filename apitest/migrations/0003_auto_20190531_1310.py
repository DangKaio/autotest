# Generated by Django 2.2.1 on 2019-05-31 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20190531_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api_test_step',
            options={'verbose_name': '操作步骤', 'verbose_name_plural': '操作步骤'},
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apimethod',
            field=models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='请求方法'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apiname',
            field=models.CharField(max_length=100, verbose_name='接口名称'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apiparamvalue',
            field=models.CharField(max_length=800, verbose_name='请求参数和值'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apiresponse',
            field=models.CharField(max_length=5000, null=True, verbose_name='响应数据'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apiresult',
            field=models.CharField(max_length=200, verbose_name='预期结果'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apistatus',
            field=models.BooleanField(verbose_name='是否通过'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apistep',
            field=models.CharField(max_length=100, null=True, verbose_name='测试步骤'),
        ),
        migrations.AlterField(
            model_name='api_test_step',
            name='apiurl',
            field=models.CharField(max_length=200, verbose_name='url地址'),
        ),
    ]
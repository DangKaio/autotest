from django.db import models

# Create your models here.


class Product(models.Model):
    """产品"""
    productname=models.CharField('产品名称',max_length=64)
    productdesc = models.CharField('产品描述', max_length=64)
    producter = models.CharField('产品负责人', max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now=True) # 自动获取当前时间

    class Meta:
        # 设置迁移后的表名
        db_table="product"
        verbose_name='产品管理'
        verbose_name_plural='产品管理'


    def __str__(self):
        return self.productname
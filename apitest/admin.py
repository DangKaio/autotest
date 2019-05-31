from django.contrib import admin
from apitest.models import Api_Test_Case,Api_Test_Step
# Register your models here.
class ApiStepAdmin(admin.TabularInline):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','Apitest']
    model = Api_Test_Step
    extra = 1

class ApiTestAdmin(admin.ModelAdmin):
    list_display = ['id','apitestname','apitester','apitestresult','create_time']
    inlines = [ApiStepAdmin]

admin.site.register(Api_Test_Case,ApiTestAdmin)
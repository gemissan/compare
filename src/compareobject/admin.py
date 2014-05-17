from django.contrib import admin

from compareobject.models import CompareObjectType, CompareCategory, CompareObject, Comparision


class CompareObjectTypeAdmin(admin.ModelAdmin):
    
    pass


class CompareCategoryAdmin(admin.ModelAdmin):
    
    pass


class CompareObjectAdmin(admin.ModelAdmin):
    
    pass


class ComparisionAdmin(admin.ModelAdmin):
    
    pass


admin.site.register(CompareObjectType, CompareObjectTypeAdmin)
admin.site.register(CompareCategory, CompareCategoryAdmin)
admin.site.register(CompareObject, CompareObjectAdmin)
admin.site.register(Comparision, ComparisionAdmin)
from django.contrib import admin

from comparelist.models import CompareFeature, CompareList, CompareView


class CompareFeatureAdmin(admin.ModelAdmin):
    
    pass


class CompareListAdmin(admin.ModelAdmin):
    
    pass


class CompareViewAdmin(admin.ModelAdmin):
    
    pass


admin.site.register(CompareFeature, CompareFeatureAdmin)
admin.site.register(CompareList, CompareListAdmin)
admin.site.register(CompareView, CompareViewAdmin)

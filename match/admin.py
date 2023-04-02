from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Live)
admin.site.register(Highlight)
admin.site.site_header='SSL Dashboard'

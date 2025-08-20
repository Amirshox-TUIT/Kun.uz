from django.contrib import admin
from apps.kunuz.models import *

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Managers)
admin.site.register(Tags)
admin.site.register(PostCategory)

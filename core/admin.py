from django.contrib import admin
from .models import * 

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Driver)
admin.site.register(Rider)
# add abstract user later

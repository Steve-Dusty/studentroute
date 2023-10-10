from django.contrib import admin
from .models import Profile, Post, Pair

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Pair)
# add abstract user later
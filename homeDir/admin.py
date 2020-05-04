from django.contrib import admin
from users.models import Profile
from .models import MainPost
from comment.models import MainComment

admin.site.register(Profile)
admin.site.register(MainPost)
admin.site.register(MainComment)

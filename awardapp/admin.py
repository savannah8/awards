from django.contrib import admin
from .models import Project,Profile,UsabilityRating,ContentRating,DesignRating

admin.site.register(Project)
admin.site.register(ContentRating)
admin.site.register(UsabilityRating)
admin.site.register(DesignRating)
admin.site.register(Profile)


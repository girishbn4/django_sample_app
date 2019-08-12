from django.contrib import admin
from applive.models import Country
from applive.models import Language
from applive.models import Channels

# Register your models here.
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Channels)

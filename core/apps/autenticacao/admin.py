from django.contrib import admin
from .models import Usuario
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)


admin.site.register(Usuario)
admin.register(OutstandingToken)
admin.register(BlacklistedToken)
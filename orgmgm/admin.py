from django.contrib import admin

from .models import Organisation
from .models import OrganisationType
from .models import Kontakt
from .models import Bundesland
from .models import Activity
from .models import ActivityType

admin.site.register(Organisation)
admin.site.register(Kontakt)
admin.site.register(Bundesland)
admin.site.register(OrganisationType)
admin.site.register(Activity)
admin.site.register(ActivityType)


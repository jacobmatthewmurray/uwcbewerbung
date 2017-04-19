import django_tables2 as tables
from .models import Organisation

class OrgaTable(tables.Table):
    edit_column = tables.TemplateColumn('<a href="">Edit</a>', orderable=False)
    class Meta:
        model = Organisation
        attrs = {'class' : 'paleblue'}
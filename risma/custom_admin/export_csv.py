import csv

from django.db.models.sql.constants import LOOKUP_SEP
from django.http import HttpResponse
from django.template import Context, Template


def queryset_to_csv(modeladmin, request, queryset):
    """ 
        return an Httpresponse with 'text/csv' as mimetype
    """
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    w = csv.writer(response, delimiter=';')
    fields = modeladmin.csv_fields
    """
    try :
        fields = modeladmin.csv_fields
    except:
        fields = modeladmin.model._meta.fields
    """
    field_names = [field_name for field, field_name in fields]
    w.writerow(field_names)
    replace_dc = { '\n' : '* ', '\r' : '', ';' : ',', '\"' : '|', '\'' : '|'}
    
    fields = [field for field, field_name in modeladmin.csv_fields]
    queryset = modeladmin.csv_queryset
    result = []
    
    for item in queryset:
        obj = {}
        cur_item = item
        for field, field_name in modeladmin.csv_fields:
            item = cur_item
            
            field_list = field.split(LOOKUP_SEP)
            if len(field_list) > 1:
                for field_label in field_list[:-1]:
                    item = getattr(item, field_label)
                field = field_list[-1]
            try:
                value = getattr(item, field)
            except:
                value = u""
                
            if not callable(value):
                uf = unicode(value)
            else:
                uf = unicode(value())
                
            for i, j in replace_dc.iteritems():
                uf = uf.replace(i,j)
                obj[field_name] = uf
                
        result.append(obj)
#    response.write (get_csv_from_dict_list(field_names, result).encode("iso-8859-1"))
    response.write (get_csv_from_dict_list(field_names, result))
    return response 
queryset_to_csv.short_description = "Exporter en csv"


def get_csv_from_dict_list(field_list, data):
    csv_line = ";".join(['{{ row.%s|addslashes|safe }}' % field for field in field_list])
    template = "{% for row in data %}" + csv_line + "\n{% endfor %}"
    return Template(template).render(Context({"data" : data}))
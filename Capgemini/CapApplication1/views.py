from importlib import import_module

from django.http import HttpResponse, HttpResponseNotFound

ANCHOR = '<a href="{mod_name}/{obj_name}">{text}</a>'

def mod_handler(request, mod_name):
    try:
        mod = import_module(mod_name)
        names = (ANCHOR.format(mod_name=mod_name, obj_name=name, text=name)for name in dir(mod) if not name.startswith('_'))
        html = '<br>'.join(names)
        return HttpResponse(html)
    except ImportError as e:
        return HttpResponseNotFound(e)

def obj_handler(request, mod_name, obj_name):
    try:
        mod = import_module(mod_name)
        obj = getattr(mod, obj_name)
        html = '<br>'.join(dir(obj))
        return HttpResponse(html)
    except ImportError as e:
        return HttpResponseNotFound(e)
    except AttributeError as e:
        return HttpResponseNotFound(e)
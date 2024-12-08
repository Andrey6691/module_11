from pprint import pprint
import inspect

def introspection_info(obj):
    info = {'type' : [], 'methods' : [], 'attributes' : [],'module' : []}
    info['type'].append(type(obj))
    for i in dir(obj):
        if callable(getattr(obj, i)):
            info['methods'].append(i)
        else:
            info['attributes'].append(i)
    module = inspect.getmodule(obj)
    if module is None:
        info['module'] = __name__
    else:
        info['module'] = module.__name__

    return info


number_info = introspection_info(42)
pprint(number_info)






import sys
from pprint import pprint 

sys.path.append("./strategy/")

#def onbar(obj):
#    from pdb import set_trace
#    pdb.set_trace()
module = __import__('bband')
if hasattr(module, 'bband'):
    o_cls = getattr(module, 'bband')

def onbar(obj):
    o = o_cls()
    if hasattr(o, 'onbar'):
        func = getattr(o, 'onbar')
#        pprint(obj)
        func(obj)
    else:
        raise Exception('method not exists')


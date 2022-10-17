from datetime import datetime,timezone
import sys, os, inspect

from flask import g

# print(datetime.datetime.now(),__name__,'--handler','new_user',g.vg['log'])

def log(name,*args):
    '''
    name: __name__
    default:
        <hora> <log> <name_function>
    '''
    _g = '-'
    # if g.vg and 'log' in g.vg:
    if g and 'vg' in g and 'log' in g.vg:
        _g = g.vg['log']
    _function_name = '-'
    stack_list = inspect.stack()
    if len(stack_list)>1:
        frame,filename,line_number,function_name,lines,index = stack_list[1]
        _function_name = function_name
    print(datetime.now(timezone.utc).isoformat(),_g,name,_function_name,*args)

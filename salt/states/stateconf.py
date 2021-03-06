'''
Stateconf System
================

The stateconf system is inteded for use only with the stateconf renderer. This
State module presents the set function. This function does not execute any
functionality, but is used to interact with the stateconf renderer.
'''


def _no_op(name, **kws):
    '''
    No-op state to support state config via the stateconf renderer.
    '''
    return dict(name=name, result=True, changes={}, comment='')

set = context = _no_op

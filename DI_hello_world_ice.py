# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `hello_world.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module dried_ice.example
_M_dried_ice = Ice.openModule('dried_ice')
_M_dried_ice.example = Ice.openModule('dried_ice.example')
__name__ = 'dried_ice.example'

if 'HelloWorld' not in _M_dried_ice.example.__dict__:
    _M_dried_ice.example.HelloWorld = Ice.createTempClass()
    class HelloWorld(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_dried_ice.example.HelloWorld:
                raise RuntimeError('dried_ice.example.HelloWorld is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::example::HelloWorld')

        def ice_id(self, current=None):
            return '::example::HelloWorld'

        def ice_staticId():
            return '::example::HelloWorld'
        ice_staticId = staticmethod(ice_staticId)

        def send_async(self, _cb, msg, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_dried_ice.example._t_HelloWorld)

        __repr__ = __str__

    _M_dried_ice.example.HelloWorldPrx = Ice.createTempClass()
    class HelloWorldPrx(Ice.ObjectPrx):

        def send(self, msg, _ctx=None):
            return _M_dried_ice.example.HelloWorld._op_send.invoke(self, ((msg, ), _ctx))

        def begin_send(self, msg, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_dried_ice.example.HelloWorld._op_send.begin(self, ((msg, ), _response, _ex, _sent, _ctx))

        def end_send(self, _r):
            return _M_dried_ice.example.HelloWorld._op_send.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_dried_ice.example.HelloWorldPrx.ice_checkedCast(proxy, '::example::HelloWorld', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_dried_ice.example.HelloWorldPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_dried_ice.example._t_HelloWorldPrx = IcePy.defineProxy('::example::HelloWorld', HelloWorldPrx)

    _M_dried_ice.example._t_HelloWorld = IcePy.defineClass('::example::HelloWorld', HelloWorld, -1, (), True, False, None, (), ())
    HelloWorld._ice_type = _M_dried_ice.example._t_HelloWorld

    HelloWorld._op_send = IcePy.Operation('send', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_dried_ice.example.HelloWorld = HelloWorld
    del HelloWorld

    _M_dried_ice.example.HelloWorldPrx = HelloWorldPrx
    del HelloWorldPrx

# End of module dried_ice.example

Ice.sliceChecksums["::example::HelloWorld"] = "e54da9247c3f29b7d3c737e8adc68d3b"
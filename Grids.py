__all__ = ['Grids']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'y', u'x', u'Grid'])
@Js
def PyJsHoisted_Grid_(size, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'size':size}, var)
    var.registers([u'size'])
    var.get(u"this").put(u'size', var.get(u'size'))
    var.get(u"this").put(u'startTiles', Js(2.0))
    var.get(u"this").put(u'cells', Js([]))
    var.get(u"this").callprop(u'build')
    var.get(u"this").put(u'playerTurn', var.get(u'true'))
PyJsHoisted_Grid_.func_name = u'Grid'
var.put(u'Grid', PyJsHoisted_Grid_)
pass
var.get(u'Grid').get(u'prototype').put(u'indexes', Js([]))
#for JS loop
var.put(u'x', Js(0.0))
while (var.get(u'x')<Js(4.0)):
    try:
        var.get(u'Grid').get(u'prototype').get(u'indexes').callprop(u'push', Js([]))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<Js(4.0)):
            try:
                PyJs_Object_0_ = Js({u'x':var.get(u'x'),u'y':var.get(u'y')})
                var.get(u'Grid').get(u'prototype').get(u'indexes').get(var.get(u'x')).callprop(u'push', PyJs_Object_0_)
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
    finally:
            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x', u'row'])
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<var.get(u"this").get(u'size')):
        try:
            var.put(u'row', var.get(u"this").get(u'cells').put(var.get(u'x'), Js([])))
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<var.get(u"this").get(u'size')):
                try:
                    var.get(u'row').callprop(u'push', var.get(u"null"))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'build', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'cells'])
    var.put(u'cells', var.get(u"this").callprop(u'availableCells'))
    if var.get(u'cells').get(u'length'):
        return var.get(u'cells').get(var.get(u'Math').callprop(u'floor', (var.get(u'Math').callprop(u'random')*var.get(u'cells').get(u'length'))))
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'randomAvailableCell', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'cells', u'self'])
    var.put(u'cells', Js([]))
    var.put(u'self', var.get(u"this"))
    @Js
    def PyJs_anonymous_4_(x, y, tile, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'tile':tile, u'this':this, u'arguments':arguments}, var)
        var.registers([u'y', u'x', u'tile'])
        if var.get(u'tile').neg():
            PyJs_Object_5_ = Js({u'x':var.get(u'x'),u'y':var.get(u'y')})
            var.get(u'cells').callprop(u'push', PyJs_Object_5_)
    PyJs_anonymous_4_._set_name(u'anonymous')
    var.get(u"this").callprop(u'eachCell', PyJs_anonymous_4_)
    return var.get(u'cells')
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'availableCells', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_6_(callback, this, arguments, var=var):
    var = Scope({u'this':this, u'callback':callback, u'arguments':arguments}, var)
    var.registers([u'y', u'x', u'callback'])
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<var.get(u"this").get(u'size')):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<var.get(u"this").get(u'size')):
                try:
                    var.get(u'callback')(var.get(u'x'), var.get(u'y'), var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
PyJs_anonymous_6_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'eachCell', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").callprop(u'availableCells').get(u'length').neg().neg()
PyJs_anonymous_7_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'cellsAvailable', PyJs_anonymous_7_)
@Js
def PyJs_anonymous_8_(cell, this, arguments, var=var):
    var = Scope({u'cell':cell, u'this':this, u'arguments':arguments}, var)
    var.registers([u'cell'])
    return var.get(u"this").callprop(u'cellOccupied', var.get(u'cell')).neg()
PyJs_anonymous_8_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'cellAvailable', PyJs_anonymous_8_)
@Js
def PyJs_anonymous_9_(cell, this, arguments, var=var):
    var = Scope({u'cell':cell, u'this':this, u'arguments':arguments}, var)
    var.registers([u'cell'])
    return var.get(u"this").callprop(u'cellContent', var.get(u'cell')).neg().neg()
PyJs_anonymous_9_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'cellOccupied', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(cell, this, arguments, var=var):
    var = Scope({u'cell':cell, u'this':this, u'arguments':arguments}, var)
    var.registers([u'cell'])
    if var.get(u"this").callprop(u'withinBounds', var.get(u'cell')):
        return var.get(u"this").get(u'cells').get(var.get(u'cell').get(u'x')).get(var.get(u'cell').get(u'y'))
    else:
        return var.get(u"null")
PyJs_anonymous_10_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'cellContent', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_11_(tile, this, arguments, var=var):
    var = Scope({u'tile':tile, u'this':this, u'arguments':arguments}, var)
    var.registers([u'tile'])
    var.get(u"this").get(u'cells').get(var.get(u'tile').get(u'x')).put(var.get(u'tile').get(u'y'), var.get(u'tile'))
PyJs_anonymous_11_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'insertTile', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(tile, this, arguments, var=var):
    var = Scope({u'tile':tile, u'this':this, u'arguments':arguments}, var)
    var.registers([u'tile'])
    var.get(u"this").get(u'cells').get(var.get(u'tile').get(u'x')).put(var.get(u'tile').get(u'y'), var.get(u"null"))
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'removeTile', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(position, this, arguments, var=var):
    var = Scope({u'this':this, u'position':position, u'arguments':arguments}, var)
    var.registers([u'position'])
    return ((((var.get(u'position').get(u'x')>=Js(0.0)) and (var.get(u'position').get(u'x')<var.get(u"this").get(u'size'))) and (var.get(u'position').get(u'y')>=Js(0.0))) and (var.get(u'position').get(u'y')<var.get(u"this").get(u'size')))
PyJs_anonymous_13_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'withinBounds', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_14_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.put(u'newGrid', var.get(u'Grid').create(var.get(u"this").get(u'size')))
    var.get(u'newGrid').put(u'playerTurn', var.get(u"this").get(u'playerTurn'))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<var.get(u"this").get(u'size')):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<var.get(u"this").get(u'size')):
                try:
                    if var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')):
                        var.get(u'newGrid').callprop(u'insertTile', var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).callprop(u'clone'))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'newGrid')
PyJs_anonymous_14_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'clone', PyJs_anonymous_14_)
@Js
def PyJs_anonymous_15_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'i'])
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u"this").get(u'startTiles')):
        try:
            var.get(u"this").callprop(u'addRandomTile')
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
PyJs_anonymous_15_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'addStartTiles', PyJs_anonymous_15_)
@Js
def PyJs_anonymous_16_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'tile', u'value'])
    if var.get(u"this").callprop(u'cellsAvailable'):
        var.put(u'value', (Js(2.0) if (var.get(u'Math').callprop(u'random')<Js(0.9)) else Js(4.0)))
        var.put(u'tile', var.get(u'Tile').create(var.get(u"this").callprop(u'randomAvailableCell'), var.get(u'value')))
        var.get(u"this").callprop(u'insertTile', var.get(u'tile'))
PyJs_anonymous_16_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'addRandomTile', PyJs_anonymous_16_)
@Js
def PyJs_anonymous_17_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_18_(x, y, tile, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'tile':tile, u'this':this, u'arguments':arguments}, var)
        var.registers([u'y', u'x', u'tile'])
        if var.get(u'tile'):
            var.get(u'tile').put(u'mergedFrom', var.get(u"null"))
            var.get(u'tile').callprop(u'savePosition')
    PyJs_anonymous_18_._set_name(u'anonymous')
    var.get(u"this").callprop(u'eachCell', PyJs_anonymous_18_)
PyJs_anonymous_17_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'prepareTiles', PyJs_anonymous_17_)
@Js
def PyJs_anonymous_19_(tile, cell, this, arguments, var=var):
    var = Scope({u'tile':tile, u'cell':cell, u'this':this, u'arguments':arguments}, var)
    var.registers([u'tile', u'cell'])
    var.get(u"this").get(u'cells').get(var.get(u'tile').get(u'x')).put(var.get(u'tile').get(u'y'), var.get(u"null"))
    var.get(u"this").get(u'cells').get(var.get(u'cell').get(u'x')).put(var.get(u'cell').get(u'y'), var.get(u'tile'))
    var.get(u'tile').callprop(u'updatePosition', var.get(u'cell'))
PyJs_anonymous_19_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'moveTile', PyJs_anonymous_19_)
PyJs_Object_21_ = Js({u'x':Js(0.0),u'y':(-Js(1.0))})
PyJs_Object_22_ = Js({u'x':Js(1.0),u'y':Js(0.0)})
PyJs_Object_23_ = Js({u'x':Js(0.0),u'y':Js(1.0)})
PyJs_Object_24_ = Js({u'x':(-Js(1.0)),u'y':Js(0.0)})
PyJs_Object_20_ = Js({u'0':PyJs_Object_21_,u'1':PyJs_Object_22_,u'2':PyJs_Object_23_,u'3':PyJs_Object_24_})
var.get(u'Grid').get(u'prototype').put(u'vectors', PyJs_Object_20_)
@Js
def PyJs_anonymous_25_(direction, this, arguments, var=var):
    var = Scope({u'this':this, u'direction':direction, u'arguments':arguments}, var)
    var.registers([u'direction'])
    return var.get(u"this").get(u'vectors').get(var.get(u'direction'))
PyJs_anonymous_25_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'getVector', PyJs_anonymous_25_)
@Js
def PyJs_anonymous_26_(direction, this, arguments, var=var):
    var = Scope({u'this':this, u'direction':direction, u'arguments':arguments}, var)
    var.registers([u'direction', u'score', u'won', u'self', u'traversals', u'moved', u'cell', u'vector', u'tile'])
    var.put(u'self', var.get(u"this"))
    pass
    var.put(u'vector', var.get(u"this").callprop(u'getVector', var.get(u'direction')))
    var.put(u'traversals', var.get(u"this").callprop(u'buildTraversals', var.get(u'vector')))
    var.put(u'moved', Js(False))
    var.put(u'score', Js(0.0))
    var.put(u'won', Js(False))
    var.get(u"this").callprop(u'prepareTiles')
    @Js
    def PyJs_anonymous_27_(x, this, arguments, var=var):
        var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
        var.registers([u'x'])
        @Js
        def PyJs_anonymous_28_(y, this, arguments, var=var):
            var = Scope({u'y':y, u'this':this, u'arguments':arguments}, var)
            var.registers([u'y', u'positions', u'merged', u'next'])
            var.put(u'cell', var.get(u'self').get(u'indexes').get(var.get(u'x')).get(var.get(u'y')))
            var.put(u'tile', var.get(u'self').callprop(u'cellContent', var.get(u'cell')))
            if var.get(u'tile'):
                var.put(u'positions', var.get(u'self').callprop(u'findFarthestPosition', var.get(u'cell'), var.get(u'vector')))
                var.put(u'next', var.get(u'self').callprop(u'cellContent', var.get(u'positions').get(u'next')))
                if ((var.get(u'next') and PyJsStrictEq(var.get(u'next').get(u'value'),var.get(u'tile').get(u'value'))) and var.get(u'next').get(u'mergedFrom').neg()):
                    var.put(u'merged', var.get(u'Tile').create(var.get(u'positions').get(u'next'), (var.get(u'tile').get(u'value')*Js(2.0))))
                    var.get(u'merged').put(u'mergedFrom', Js([var.get(u'tile'), var.get(u'next')]))
                    var.get(u'self').callprop(u'insertTile', var.get(u'merged'))
                    var.get(u'self').callprop(u'removeTile', var.get(u'tile'))
                    var.get(u'tile').callprop(u'updatePosition', var.get(u'positions').get(u'next'))
                    var.put(u'score', var.get(u'merged').get(u'value'), u'+')
                    if PyJsStrictEq(var.get(u'merged').get(u'value'),Js(2048.0)):
                        var.put(u'won', var.get(u'true'))
                else:
                    var.get(u'self').callprop(u'moveTile', var.get(u'tile'), var.get(u'positions').get(u'farthest'))
                if var.get(u'self').callprop(u'positionsEqual', var.get(u'cell'), var.get(u'tile')).neg():
                    var.get(u'self').put(u'playerTurn', Js(False))
                    var.put(u'moved', var.get(u'true'))
        PyJs_anonymous_28_._set_name(u'anonymous')
        var.get(u'traversals').get(u'y').callprop(u'forEach', PyJs_anonymous_28_)
    PyJs_anonymous_27_._set_name(u'anonymous')
    var.get(u'traversals').get(u'x').callprop(u'forEach', PyJs_anonymous_27_)
    PyJs_Object_29_ = Js({u'moved':var.get(u'moved'),u'score':var.get(u'score'),u'won':var.get(u'won')})
    return PyJs_Object_29_
PyJs_anonymous_26_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'move', PyJs_anonymous_26_)
@Js
def PyJs_anonymous_30_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").callprop(u'addRandomTile')
    var.get(u"this").put(u'playerTurn', var.get(u'true'))
PyJs_anonymous_30_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'computerMove', PyJs_anonymous_30_)
@Js
def PyJs_anonymous_31_(vector, this, arguments, var=var):
    var = Scope({u'this':this, u'vector':vector, u'arguments':arguments}, var)
    var.registers([u'vector', u'traversals', u'pos'])
    PyJs_Object_32_ = Js({u'x':Js([]),u'y':Js([])})
    var.put(u'traversals', PyJs_Object_32_)
    #for JS loop
    var.put(u'pos', Js(0.0))
    while (var.get(u'pos')<var.get(u"this").get(u'size')):
        try:
            var.get(u'traversals').get(u'x').callprop(u'push', var.get(u'pos'))
            var.get(u'traversals').get(u'y').callprop(u'push', var.get(u'pos'))
        finally:
                (var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1))
    if PyJsStrictEq(var.get(u'vector').get(u'x'),Js(1.0)):
        var.get(u'traversals').put(u'x', var.get(u'traversals').get(u'x').callprop(u'reverse'))
    if PyJsStrictEq(var.get(u'vector').get(u'y'),Js(1.0)):
        var.get(u'traversals').put(u'y', var.get(u'traversals').get(u'y').callprop(u'reverse'))
    return var.get(u'traversals')
PyJs_anonymous_31_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'buildTraversals', PyJs_anonymous_31_)
@Js
def PyJs_anonymous_33_(cell, vector, this, arguments, var=var):
    var = Scope({u'cell':cell, u'this':this, u'vector':vector, u'arguments':arguments}, var)
    var.registers([u'cell', u'vector', u'previous'])
    pass
    while 1:
        var.put(u'previous', var.get(u'cell'))
        PyJs_Object_34_ = Js({u'x':(var.get(u'previous').get(u'x')+var.get(u'vector').get(u'x')),u'y':(var.get(u'previous').get(u'y')+var.get(u'vector').get(u'y'))})
        var.put(u'cell', PyJs_Object_34_)
        if not (var.get(u"this").callprop(u'withinBounds', var.get(u'cell')) and var.get(u"this").callprop(u'cellAvailable', var.get(u'cell'))):
            break
    PyJs_Object_35_ = Js({u'farthest':var.get(u'previous'),u'next':var.get(u'cell')})
    return PyJs_Object_35_
PyJs_anonymous_33_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'findFarthestPosition', PyJs_anonymous_33_)
@Js
def PyJs_anonymous_36_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return (var.get(u"this").callprop(u'cellsAvailable') or var.get(u"this").callprop(u'tileMatchesAvailable'))
PyJs_anonymous_36_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'movesAvailable', PyJs_anonymous_36_)
@Js
def PyJs_anonymous_37_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'direction', u'self', u'cell', u'y', u'vector', u'tile', u'x', u'other'])
    var.put(u'self', var.get(u"this"))
    pass
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<var.get(u"this").get(u'size')):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<var.get(u"this").get(u'size')):
                try:
                    PyJs_Object_38_ = Js({u'x':var.get(u'x'),u'y':var.get(u'y')})
                    var.put(u'tile', var.get(u"this").callprop(u'cellContent', PyJs_Object_38_))
                    if var.get(u'tile'):
                        #for JS loop
                        var.put(u'direction', Js(0.0))
                        while (var.get(u'direction')<Js(4.0)):
                            try:
                                var.put(u'vector', var.get(u'self').callprop(u'getVector', var.get(u'direction')))
                                PyJs_Object_39_ = Js({u'x':(var.get(u'x')+var.get(u'vector').get(u'x')),u'y':(var.get(u'y')+var.get(u'vector').get(u'y'))})
                                var.put(u'cell', PyJs_Object_39_)
                                var.put(u'other', var.get(u'self').callprop(u'cellContent', var.get(u'cell')))
                                if (var.get(u'other') and PyJsStrictEq(var.get(u'other').get(u'value'),var.get(u'tile').get(u'value'))):
                                    return var.get(u'true')
                            finally:
                                    (var.put(u'direction',Js(var.get(u'direction').to_number())+Js(1))-Js(1))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return Js(False)
PyJs_anonymous_37_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'tileMatchesAvailable', PyJs_anonymous_37_)
@Js
def PyJs_anonymous_40_(first, second, this, arguments, var=var):
    var = Scope({u'this':this, u'second':second, u'arguments':arguments, u'first':first}, var)
    var.registers([u'second', u'first'])
    return (PyJsStrictEq(var.get(u'first').get(u'x'),var.get(u'second').get(u'x')) and PyJsStrictEq(var.get(u'first').get(u'y'),var.get(u'second').get(u'y')))
PyJs_anonymous_40_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'positionsEqual', PyJs_anonymous_40_)
@Js
def PyJs_anonymous_41_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'i', u'j'])
    var.put(u'string', Js(u''))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'j', Js(0.0))
            while (var.get(u'j')<Js(4.0)):
                try:
                    if var.get(u"this").get(u'cells').get(var.get(u'j')).get(var.get(u'i')):
                        var.put(u'string', (var.get(u"this").get(u'cells').get(var.get(u'j')).get(var.get(u'i')).get(u'value')+Js(u' ')), u'+')
                    else:
                        var.put(u'string', Js(u'_ '), u'+')
                finally:
                        (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
            var.put(u'string', Js(u'\n'), u'+')
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'string')
PyJs_anonymous_41_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'toString', PyJs_anonymous_41_)
@Js
def PyJs_anonymous_42_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'islands', u'self', u'x', u'mark'])
    var.put(u'self', var.get(u"this"))
    @Js
    def PyJs_anonymous_43_(x, y, value, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'y', u'x', u'vector', u'value'])
        if (((((((var.get(u'x')>=Js(0.0)) and (var.get(u'x')<=Js(3.0))) and (var.get(u'y')>=Js(0.0))) and (var.get(u'y')<=Js(3.0))) and var.get(u'self').get(u'cells').get(var.get(u'x')).get(var.get(u'y'))) and (var.get(u'self').get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'value')==var.get(u'value'))) and var.get(u'self').get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'marked').neg()):
            var.get(u'self').get(u'cells').get(var.get(u'x')).get(var.get(u'y')).put(u'marked', var.get(u'true'))
            for PyJsTemp in Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0)]):
                var.put(u'direction', PyJsTemp)
                var.put(u'vector', var.get(u'self').callprop(u'getVector', var.get(u'direction')))
                var.get(u'mark')((var.get(u'x')+var.get(u'vector').get(u'x')), (var.get(u'y')+var.get(u'vector').get(u'y')), var.get(u'value'))
    PyJs_anonymous_43_._set_name(u'anonymous')
    var.put(u'mark', PyJs_anonymous_43_)
    var.put(u'islands', Js(0.0))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    if var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')):
                        var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).put(u'marked', Js(False))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    if (var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')) and var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'marked').neg()):
                        (var.put(u'islands',Js(var.get(u'islands').to_number())+Js(1))-Js(1))
                        PyJs_Object_44_ = Js({u'x':var.get(u'x'),u'y':var.get(u'y')})
                        var.get(u'mark')(PyJs_Object_44_, var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'value'))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'islands')
PyJs_anonymous_42_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'islands', PyJs_anonymous_42_)
@Js
def PyJs_anonymous_45_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'direction', u'target', u'value', u'targetCell', u'vector', u'targetValue', u'y', u'x', u'smoothness'])
    var.put(u'smoothness', Js(0.0))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    if var.get(u"this").callprop(u'cellOccupied', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))):
                        var.put(u'value', (var.get(u'Math').callprop(u'log', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))))
                        #for JS loop
                        var.put(u'direction', Js(1.0))
                        while (var.get(u'direction')<=Js(2.0)):
                            try:
                                var.put(u'vector', var.get(u"this").callprop(u'getVector', var.get(u'direction')))
                                var.put(u'targetCell', var.get(u"this").callprop(u'findFarthestPosition', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y')), var.get(u'vector')).get(u'next'))
                                if var.get(u"this").callprop(u'cellOccupied', var.get(u'targetCell')):
                                    var.put(u'target', var.get(u"this").callprop(u'cellContent', var.get(u'targetCell')))
                                    var.put(u'targetValue', (var.get(u'Math').callprop(u'log', var.get(u'target').get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))))
                                    var.put(u'smoothness', var.get(u'Math').callprop(u'abs', (var.get(u'value')-var.get(u'targetValue'))), u'-')
                            finally:
                                    (var.put(u'direction',Js(var.get(u'direction').to_number())+Js(1))-Js(1))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'smoothness')
PyJs_anonymous_45_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'smoothness', PyJs_anonymous_45_)
@Js
def PyJs_anonymous_46_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'highestCell', u'self', u'markAndScore', u'marked', u'highestValue', u'y', u'x', u'queued'])
    var.put(u'self', var.get(u"this"))
    var.put(u'marked', Js([]))
    var.put(u'queued', Js([]))
    var.put(u'highestValue', Js(0.0))
    PyJs_Object_47_ = Js({u'x':Js(0.0),u'y':Js(0.0)})
    var.put(u'highestCell', PyJs_Object_47_)
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            var.get(u'marked').callprop(u'push', Js([]))
            var.get(u'queued').callprop(u'push', Js([]))
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    var.get(u'marked').get(var.get(u'x')).callprop(u'push', Js(False))
                    var.get(u'queued').get(var.get(u'x')).callprop(u'push', Js(False))
                    if (var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')) and (var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'value')>var.get(u'highestValue'))):
                        var.put(u'highestValue', var.get(u"this").get(u'cells').get(var.get(u'x')).get(var.get(u'y')).get(u'value'))
                        var.get(u'highestCell').put(u'x', var.get(u'x'))
                        var.get(u'highestCell').put(u'y', var.get(u'y'))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    var.put(u'increases', Js(0.0))
    var.put(u'cellQueue', Js([var.get(u'highestCell')]))
    var.get(u'queued').get(var.get(u'highestCell').get(u'x')).put(var.get(u'highestCell').get(u'y'), var.get(u'true'))
    var.put(u'markList', Js([var.get(u'highestCell')]))
    var.put(u'markAfter', Js(1.0))
    @Js
    def PyJs_anonymous_48_(cell, this, arguments, var=var):
        var = Scope({u'cell':cell, u'this':this, u'arguments':arguments}, var)
        var.registers([u'cell', u'cel', u'vector', u'target', u'value'])
        var.get(u'markList').callprop(u'push', var.get(u'cell'))
        pass
        if var.get(u'self').callprop(u'cellOccupied', var.get(u'cell')):
            var.put(u'value', (var.get(u'Math').callprop(u'log', var.get(u'self').callprop(u'cellContent', var.get(u'cell')).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))))
        else:
            var.put(u'value', Js(0.0))
        for PyJsTemp in Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0)]):
            var.put(u'direction', PyJsTemp)
            var.put(u'vector', var.get(u'self').callprop(u'getVector', var.get(u'direction')))
            PyJs_Object_49_ = Js({u'x':(var.get(u'cell').get(u'x')+var.get(u'vector').get(u'x')),u'y':(var.get(u'cell').get(u'y')+var.get(u'vector').get(u'y'))})
            var.put(u'target', PyJs_Object_49_)
            if (var.get(u'self').callprop(u'withinBounds', var.get(u'target')) and var.get(u'marked').get(var.get(u'target').get(u'x')).get(var.get(u'target').get(u'y')).neg()):
                if var.get(u'self').callprop(u'cellOccupied', var.get(u'target')):
                    var.put(u'targetValue', (var.get(u'Math').callprop(u'log', var.get(u'self').callprop(u'cellContent', var.get(u'target')).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))))
                    if (var.get(u'targetValue')>var.get(u'value')):
                        var.put(u'increases', (var.get(u'targetValue')-var.get(u'value')), u'+')
                if var.get(u'queued').get(var.get(u'target').get(u'x')).get(var.get(u'target').get(u'y')).neg():
                    var.get(u'cellQueue').callprop(u'push', var.get(u'target'))
                    var.get(u'queued').get(var.get(u'target').get(u'x')).put(var.get(u'target').get(u'y'), var.get(u'true'))
        if (var.get(u'markAfter')==Js(0.0)):
            while (var.get(u'markList').get(u'length')>Js(0.0)):
                var.put(u'cel', var.get(u'markList').callprop(u'pop'))
                var.get(u'marked').get(var.get(u'cel').get(u'x')).put(var.get(u'cel').get(u'y'), var.get(u'true'))
            var.put(u'markAfter', var.get(u'cellQueue').get(u'length'))
    PyJs_anonymous_48_._set_name(u'anonymous')
    var.put(u'markAndScore', PyJs_anonymous_48_)
    while (var.get(u'cellQueue').get(u'length')>Js(0.0)):
        (var.put(u'markAfter',Js(var.get(u'markAfter').to_number())-Js(1))+Js(1))
        var.get(u'markAndScore')(var.get(u'cellQueue').callprop(u'shift'))
    return (-var.get(u'increases'))
PyJs_anonymous_46_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'monotonicity', PyJs_anonymous_46_)
@Js
def PyJs_anonymous_50_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'currentValue', u'next', u'current', u'nextValue', u'y', u'x', u'totals'])
    var.put(u'totals', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            var.put(u'current', Js(0.0))
            var.put(u'next', (var.get(u'current')+Js(1.0)))
            while (var.get(u'next')<Js(4.0)):
                while ((var.get(u'next')<Js(4.0)) and var.get(u"this").callprop(u'cellOccupied', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'next'))).neg()):
                    (var.put(u'next',Js(var.get(u'next').to_number())+Js(1))-Js(1))
                if (var.get(u'next')>=Js(4.0)):
                    (var.put(u'next',Js(var.get(u'next').to_number())-Js(1))+Js(1))
                PyJs_Object_51_ = Js({u'x':var.get(u'x'),u'y':var.get(u'current')})
                var.put(u'currentValue', ((var.get(u'Math').callprop(u'log', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'current'))).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))) if var.get(u"this").callprop(u'cellOccupied', PyJs_Object_51_) else Js(0.0)))
                PyJs_Object_52_ = Js({u'x':var.get(u'x'),u'y':var.get(u'next')})
                var.put(u'nextValue', ((var.get(u'Math').callprop(u'log', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'next'))).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))) if var.get(u"this").callprop(u'cellOccupied', PyJs_Object_52_) else Js(0.0)))
                if (var.get(u'currentValue')>var.get(u'nextValue')):
                    var.get(u'totals').put(u'0', (var.get(u'nextValue')-var.get(u'currentValue')), u'+')
                else:
                    if (var.get(u'nextValue')>var.get(u'currentValue')):
                        var.get(u'totals').put(u'1', (var.get(u'currentValue')-var.get(u'nextValue')), u'+')
                var.put(u'current', var.get(u'next'))
                (var.put(u'next',Js(var.get(u'next').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put(u'y', Js(0.0))
    while (var.get(u'y')<Js(4.0)):
        try:
            var.put(u'current', Js(0.0))
            var.put(u'next', (var.get(u'current')+Js(1.0)))
            while (var.get(u'next')<Js(4.0)):
                while ((var.get(u'next')<Js(4.0)) and var.get(u"this").callprop(u'cellOccupied', var.get(u"this").get(u'indexes').get(var.get(u'next')).get(var.get(u'y'))).neg()):
                    (var.put(u'next',Js(var.get(u'next').to_number())+Js(1))-Js(1))
                if (var.get(u'next')>=Js(4.0)):
                    (var.put(u'next',Js(var.get(u'next').to_number())-Js(1))+Js(1))
                PyJs_Object_53_ = Js({u'x':var.get(u'current'),u'y':var.get(u'y')})
                var.put(u'currentValue', ((var.get(u'Math').callprop(u'log', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'current')).get(var.get(u'y'))).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))) if var.get(u"this").callprop(u'cellOccupied', PyJs_Object_53_) else Js(0.0)))
                PyJs_Object_54_ = Js({u'x':var.get(u'next'),u'y':var.get(u'y')})
                var.put(u'nextValue', ((var.get(u'Math').callprop(u'log', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'next')).get(var.get(u'y'))).get(u'value'))/var.get(u'Math').callprop(u'log', Js(2.0))) if var.get(u"this").callprop(u'cellOccupied', PyJs_Object_54_) else Js(0.0)))
                if (var.get(u'currentValue')>var.get(u'nextValue')):
                    var.get(u'totals').put(u'2', (var.get(u'nextValue')-var.get(u'currentValue')), u'+')
                else:
                    if (var.get(u'nextValue')>var.get(u'currentValue')):
                        var.get(u'totals').put(u'3', (var.get(u'currentValue')-var.get(u'nextValue')), u'+')
                var.put(u'current', var.get(u'next'))
                (var.put(u'next',Js(var.get(u'next').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
    return (var.get(u'Math').callprop(u'max', var.get(u'totals').get(u'0'), var.get(u'totals').get(u'1'))+var.get(u'Math').callprop(u'max', var.get(u'totals').get(u'2'), var.get(u'totals').get(u'3')))
PyJs_anonymous_50_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'monotonicity2', PyJs_anonymous_50_)
@Js
def PyJs_anonymous_55_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'max', u'value', u'x'])
    var.put(u'max', Js(0.0))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    if var.get(u"this").callprop(u'cellOccupied', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))):
                        var.put(u'value', var.get(u"this").callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))).get(u'value'))
                        if (var.get(u'value')>var.get(u'max')):
                            var.put(u'max', var.get(u'value'))
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return (var.get(u'Math').callprop(u'log', var.get(u'max'))/var.get(u'Math').callprop(u'log', Js(2.0)))
PyJs_anonymous_55_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'maxValue', PyJs_anonymous_55_)
@Js
def PyJs_anonymous_56_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x', u'self'])
    var.put(u'self', var.get(u"this"))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(4.0)):
        try:
            #for JS loop
            var.put(u'y', Js(0.0))
            while (var.get(u'y')<Js(4.0)):
                try:
                    if var.get(u'self').callprop(u'cellOccupied', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))):
                        if (var.get(u'self').callprop(u'cellContent', var.get(u"this").get(u'indexes').get(var.get(u'x')).get(var.get(u'y'))).get(u'value')==Js(2048.0)):
                            return var.get(u'true')
                finally:
                        (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return Js(False)
PyJs_anonymous_56_._set_name(u'anonymous')
var.get(u'Grid').get(u'prototype').put(u'isWin', PyJs_anonymous_56_)


# Add lib to the module scope
Grids = var.to_python()
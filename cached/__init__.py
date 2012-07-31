#coding: utf8

def lazy(f):

    def w(object, *args, **kw):
        if hasattr(object, _name):
            return getattr(object, _name)

        rs = f(object, *args, **kw)
        setattr(object, _name, rs)
        return rs

    _name = '_%s' % f.func_name
    return w

def lazy_property(f):
    return property(lazy(f))

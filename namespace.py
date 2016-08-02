import collections

class namespace(dict):
    protected = []
    
    def __init__(self, *args, **kw):
        super(nook, self).__init__(*args, **kw)
        self.protected = set(dir(self))
        for key in self:
            setattr(self, key, self[key])
        
    def __setitem__(self, key, value):
        setattr(self, key, value)
        super(nook, self).__setitem__(key, value)
        
    def __setattr__(self, key, value):
        if key in self.protected:
            raise ValueError('Key entries cannot conflict with protected names')
        super(nook, self).__setattr__(key, value)
        
    def setdefault(self, key, default=None):
        val = super(nook, self).setdefault(key, default)
        setattr(self, key, val)
        return val
    
    def update(self, other=None, **kwargs):
        # super(namespace, self).update(*args, **kwargs)
        # for k, v in self.iteritems():
        #     self[k] = v
        if isinstance(other, dict):
            for k, v in other.iteritems():
                self[k] = v
        elif other:
            for x, item in enumerate(other):
                if not isinstance(item, collections.Sequence):
                    raise TypeError('cannot convert dictionary update sequence element'
                                    ' #{} to a sequence'.format(x))
                if len(item) != 2:
                    raise ValueError('dictionary update sequence element #{} has length'
                                     ' {}; 2 is required'.format(x, len(item)))
                self[item[0]] = item[1]
        for k, v in kwargs.iteritems():
            self[k] = v
        
        
    def __delitem__(self, key):
        super(nook, self).__delitem__(key)
        delattr(self, key)
        
    def clear(self):
        super(nook, self).clear()
        for key in self:
            delattr(self, key)
            
    def pop(self, key, *args, **kwargs):
        val = super(nook, self).pop(key, *args, **kwargs)
        if hasattr(self, key):
            delattr(self, key)
        return val
    
    def popitem(self):
        pair = super(nook, self).popitem()
        delattr(self, pair[0])
        return pair

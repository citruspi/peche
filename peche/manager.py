#!/usr/bin/env python
# -*- coding: utf8 -*-

import inspect
from peche.context import Context

class Manager(object):
    __state = {}
    contexts = {}

    def __init__(self):
        self.__dict__ = self.__state

    def setup(self, name=None, root=None):
        if name is None or root is None:
            path = inspect.stack()[1][1]

            components = path.split('/')

            name = name or components[-2]
            root = root or '/'.join(components[0:-1])

        try:
            context = self.contexts[name]
            return context
        except KeyError:
            pass

        context = Context(name, root)

        self.contexts[name] = context

        return context
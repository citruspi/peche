#!/usr/bin/env python
# -*- coding: utf8 -*-

class Context(object):
    root = None
    name = None

    def __init__(self, name, root):
        self.name = name
        self.root = root
#!/usr/bin/env python
# -*- coding: utf8 -*-

from peche.logging import level

class Handler(object):

    levels = [level.Debug, level.Info, level.Warn, level.Error,
              level.Critical]

    def on_event(self, event):
        pass
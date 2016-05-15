#!/usr/bin/env python
# -*- coding: utf8 -*-

from peche.logging import Level

class Handler(object):

    levels = [Level.Debug, Level.Info, Level.Warn, Level.Error,
              Level.Critical]

    def on_event(self, event):
        pass
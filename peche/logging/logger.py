#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import inspect
from peche.logging import level
from peche.logging import Event

class Logger(object):

    def __init__(self, ctx):
        self.ctx = ctx
        self._handlers = []

    def add_handler(self, handler):
        self._handlers.append(handler)

    def remove_handler(self, handler):
        if handler in self._handlers:
            self._handlers.remove(handler)

    def _log(self, level_, event, **kwargs):
        timestamp = datetime.datetime.utcnow()

        stack = inspect.stack()[2]

        path = stack[1]
        line_no = stack[2]
        function = stack[3]

        path = path[len(self.ctx.root)+1:-3].replace('/', '.')

        event = Event(
            timestamp=timestamp,
            level=level_,
            ctx=self.ctx,
            function=function,
            path=path if path != '' else None,
            line_no=line_no,
            message=event,
            tags=kwargs
        )

        for handler in self._handlers:
            handler(event)

    def debug(self, event=None, **kwargs):
        self._log(level.Debug, event, **kwargs)

    def info(self, event=None, **kwargs):
        self._log(level.Info, event, **kwargs)

    def warn(self, event=None, **kwargs):
        self._log(level.Warn, event, **kwargs)

    def error(self, event=None, **kwargs):
        self._log(level.Error, event, **kwargs)

    def critical(self, event=None, **kwargs):
        self._log(level.Critical, event, **kwargs)
#!/usr/bin/env python
# -*- coding: utf8 -*-

from termcolor import cprint
from peche.logging.handlers import Handler
from peche.logging import level
from sys import stdout, stderr

class StdoutHandler(Handler):

    level_to_colour = {
        level.Debug: 'blue',
        level.Info: 'green',
        level.Warn: 'yellow',
        level.Error: 'red',
        level.Critical: 'magenta'
    }

    def __init__(self, stderr_levels=None):
        self.stderr_levels = stderr_levels or [level.Error, level.Critical]

    def template(self, event):
        template = '{timestamp}{level}{path}{message}{tags}'

        params = {
            'timestamp': '{timestamp}',
            'level': ' [{level}]',
            'path': ' {{name}}.{path}:' if event.path is not None else ' {{name}}:',
            'message': ' {message}' if event.message is not None else '',
            'tags': ' [{tags}]' if len(event.tags) > 0 else ''
        }

        if event.path is not None:
            if event.function != '<module>':
                params['path'] = params['path'].format(
                    path='{path}:{function}({line_no})')
            else:
                params['path'] = params['path'].format(
                    path='{path}({line_no})')

        template = template.format(**params)

        return template

    def format(self, template, event):
        params = {
            'timestamp': str(event.timestamp),
            'level': event.level.name.upper(),
            'message': event.message,
            'name': event.ctx.name,
            'path': event.path,
            'function': event.function,
            'line_no': event.line_no,
            'tags': '\t'.join(['{k}={v}'.format(k=k, v=event.tags[k])
                               for k in list(event.tags)]).lstrip()
        }

        return template.format(**params)

    def on_event(self, event):
        file = stderr if event.level in self.stderr_levels else stdout

        cprint(self.format(self.template(event), event),
               self.level_to_colour[event.level],
               file=file)
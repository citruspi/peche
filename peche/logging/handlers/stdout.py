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
            'path': ' {name}.{path}:' if event.path is not None else ' {name}:',
            'message': ' {message}' if event.message is not None else '',
            'tags': ' [{tags}]' if len(event.tags) > 0 else ''
        }

        template = template.format(**params)

        return template

    def on_event(self, event):
        template = self.template(event)

        if event.function != '<module>':
            path_template = '{path}:{function}({line_no})'
        else:
            path_template = '{path}({line_no})'

        params = {
            'timestamp': str(event.timestamp),
            'level': event.level.name.upper(),
            'message': event.message,
            'name': event.ctx.name,
            'path': path_template.format(path=event.path,
                                         function=event.function,
                                         line_no=event.line_no),
            'tags': '\t'.join(['{k}={v}'.format(k=k, v=event.tags[k])
                               for k in list(event.tags)]).lstrip()
        }

        file = stderr if event.level in self.stderr_levels else stdout

        cprint(template.format(**params),
               self.level_to_colour[event.level],
               file=file)
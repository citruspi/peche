#!/usr/bin/env python
# -*- coding: utf8 -*-

from peche.logging.handlers import Stdout


class TextFileHandler(Stdout):
    def __init__(self, path=None, name='peche'):
        super().__init__()

        self.path = path or '/var/log/{name}.log'.format(name=name)

    def format(self, template, event):
        return '{e}\n'.format(e=super().format(template, event))

    def on_event(self, event):
        with open(self.path, 'w') as f:
            f.write(self.format(self.template(event), event))
#!/usr/bin/env python
# -*- coding: utf8 -*-

from enum import Enum


class Level(Enum):
    Debug = 1
    Info = 2
    Warn = 3
    Error = 4
    Critical = 5
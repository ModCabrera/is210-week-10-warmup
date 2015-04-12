#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task Loop through and return dict of Heroes and Pets."""
import data


SUPER_SIDEKICKS = {}

LIMIT = 10

for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    if LIMIT > 0:
        SUPER_SIDEKICKS[HERO] = HERO_DATA.get('pet', None)
    LIMIT -= 1

#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""Copy data.BANDS dict and delete, update information."""


import data

CORRECTED = data.BANDS.copy()

CORRECTED.update({'Dylan': {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}})

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen'].update({'Sammy Hagar': ['vocals']})

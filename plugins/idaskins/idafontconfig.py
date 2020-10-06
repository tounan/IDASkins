from __future__ import absolute_import, division, print_function

import os, sys

import idaapi
from PyQt5.QtGui import QFontDatabase

_type_key_table = {
    'disas': 'Font\\Disassembly',
    'hexview': 'Font\\Hex view',
    'debug_regs': 'Font\\Debug registers',
    'text_input': 'Font\\Text input',
    'output_wnd': 'Font\\Output window',
}
# config font family
_monospace_font_family = 'Sarasa Mono TC'
_monospace_font_size = 12
_bBold, _bItalic = False, False

class IdaFontConfig(object):
    """Read access to IDA's (undocumented) font config."""
    def __init__(self, type):
        self._key = _type_key_table[type]

    @property
    def family(self):
        return _monospace_font_family
        return idaapi.reg_read_string(
            'Name',
            self._key,
            'Consolas'
            if os.name == 'nt' else 
            QFontDatabase.systemFont(QFontDatabase.FixedFont).family().encode()    
        )

    @property
    def size(self):
        return _monospace_font_size
        return idaapi.reg_read_int('Size', 10, self._key)

    @property
    def bold(self):
        return _bBold
        return idaapi.reg_read_bool('Bold', False, self._key)

    @property
    def italic(self):
        return _bItalic
        return idaapi.reg_read_bool('Italic', False, self._key)

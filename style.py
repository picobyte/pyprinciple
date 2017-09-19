# -*- coding: utf-8 -*-
"""Shared widget styles for pyprinciple

Copyright (C) 2017 Radomir Matveev GPL 3.0+
"""

# --------------------------------------------------------------------------- #
# Import libraries
# --------------------------------------------------------------------------- #
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette, QFont


# --------------------------------------------------------------------------- #
# Define classes
# --------------------------------------------------------------------------- #
class SimplePalette(QPalette):
    def __init__(self, normal, disabled, color_role=QPalette.WindowText):
        super().__init__()
        self.setBrush(QPalette.Active, color_role, normal)
        self.setBrush(QPalette.Inactive, color_role, normal)
        self.setBrush(QPalette.Disabled, color_role, disabled)


class ProgressStyle(SimplePalette):
    def __init__(self, normal):
        super().__init__(normal, dark_gray, QPalette.Highlight)


class BackgroundStyle(SimplePalette):
    def __init__(self):
        super().__init__(white, gray, QPalette.Base)
        self.setBrush(QPalette.Active, QPalette.Window, bg)
        self.setBrush(QPalette.Inactive, QPalette.Window, bg)
        self.setBrush(QPalette.Disabled, QPalette.Window, bg)


# --------------------------------------------------------------------------- #
# Define module globals
# --------------------------------------------------------------------------- #
white = QBrush(QColor(255, 255, 255, 255))
light_gray = QBrush(QColor(100, 100, 100, 255))
gray = QBrush(QColor(190, 190, 190, 255))
# TODO: looks like light_gray and gray are switched
dark_gray = QBrush(QColor(25, 25, 25, 255))
bg = QBrush(QColor(25, 45, 52, 255))
white_text = SimplePalette(white, gray)
hdr_text = SimplePalette(gray, dark_gray)

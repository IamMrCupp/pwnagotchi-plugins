"""Stub file for pwnagotchi.ui.components module"""

class LabeledValue:
    """UI component for displaying labeled values"""
    def __init__(self, color=None, label="", value="", position=(0, 0), 
                 label_font=None, text_font=None):
        self.color = color
        self.label = label
        self.value = value
        self.position = position
        self.label_font = label_font
        self.text_font = text_font

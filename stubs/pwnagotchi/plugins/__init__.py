"""Stub file for pwnagotchi.plugins module"""

class Plugin:
    """Base plugin class"""
    __author__ = ""
    __version__ = ""
    __license__ = ""
    __description__ = ""
    
    def __init__(self):
        self.ready = False
        self.options = {}
    
    def on_loaded(self):
        """Called when plugin is loaded"""
        pass
    
    def on_ready(self, agent):
        """Called when agent is ready"""
        pass
    
    def on_ui_setup(self, ui):
        """Called when UI is being set up"""
        pass
    
    def on_ui_update(self, ui):
        """Called when UI needs updating"""
        pass
    
    def on_unload(self, ui):
        """Called when plugin is unloaded"""
        pass

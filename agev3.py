import os
import json
import logging
from datetime import datetime

import pwnagotchi.plugins as plugins
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK

AGE_DATA_FILE = '/root/.pwnagotchi-age-data'

class Age(plugins.Plugin):
    __author__ = 'IamMrCupp'
    __version__ = '2.0.0'
    __license__ = 'MIT'
    __description__ = 'A simple plugin that displays the age of your pwnagotchi device on the UI.\n We display nothing more than the Age. Other plugins can be used for Str/Int/Exp/etc.'

    def __init__(self):
        self.device_start_time = None

    def on_loaded(self):
        """Load or initialize the device start time from filesystem"""
        if os.path.exists(AGE_DATA_FILE):
            try:
                with open(AGE_DATA_FILE, 'r') as f:
                    data = json.load(f)
                    self.device_start_time = datetime.fromisoformat(data['start_time'])
                    logging.info(f"[age] Loaded start time from cache: {self.device_start_time}")
            except Exception as e:
                logging.error(f"[age] Error loading age data: {e}")
                self._initialize_start_time()
        else:
            self._initialize_start_time()

    def _initialize_start_time(self):
        """Initialize device start time from filesystem and save to cache"""
        self.device_start_time = self._get_device_birth_time()
        try:
            with open(AGE_DATA_FILE, 'w') as f:
                json.dump({'start_time': self.device_start_time.isoformat()}, f)
            logging.info(f"[age] Initialized start time from filesystem: {self.device_start_time}")
        except Exception as e:
            logging.error(f"[age] Error saving age data: {e}")

    def _get_device_birth_time(self):
        """
        Determine the device's first boot time using filesystem indicators.
        Tries multiple methods in order of reliability:
        1. /home/pi/.ssh/authorized_keys
        2. /home/pi/.ssh/
        3. /root/.wget-hsts (if exists)
        """
        candidates = [
            '/home/pi/.ssh/authorized_keys',
            '/home/pi/.ssh/',
            '/root/.wget-hsts'
        ]
        
        earliest_time = None
        
        for path in candidates:
            try:
                if os.path.exists(path):
                    stat_info = os.stat(path)
                    # Use ctime (creation/change time) as it's most reliable on Linux
                    birth_time = datetime.fromtimestamp(stat_info.st_ctime)
                    
                    if earliest_time is None or birth_time < earliest_time:
                        earliest_time = birth_time
                        logging.info(f"[age] Found earlier timestamp from {path}: {birth_time}")
            except Exception as e:
                logging.error(f"[age] Error checking {path}: {e}")
                continue
        
        if earliest_time is None:
            logging.warning("[age] Could not determine device birth time, using current time")
            earliest_time = datetime.now()
        
        return earliest_time

    def on_ui_setup(self, ui):
        """Setup the Age UI element"""
        ui.add_element('Age', LabeledValue(
            color=BLACK, 
            label='♥ Age', 
            value='0d',
            position=(int(self.options.get("age_x_coord", 0)),
                      int(self.options.get("age_y_coord", 80))),
            label_font=fonts.Bold, 
            text_font=fonts.Medium
        ))

    def on_unload(self, ui):
        """Remove the Age UI element when plugin unloads"""
        with ui._lock:
            ui.remove_element('Age')

    def on_ui_update(self, ui):
        """Update the Age display"""
        if self.device_start_time:
            ui.set('Age', self.calculate_device_age())

    def calculate_device_age(self):
        """Calculate and format the device age"""
        if not self.device_start_time:
            return '0y 0m 0d'
        
        current_time = datetime.now()
        age_delta = current_time - self.device_start_time

        years = age_delta.days // 365
        remaining_days = age_delta.days % 365
        months = remaining_days // 30
        days = remaining_days % 30

        return f'{years}y {months}m {days}d'


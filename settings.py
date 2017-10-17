import os
import sys

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_VIEWS = os.path.join(APP_ROOT, 'views')
sys.path.append(APP_ROOT)
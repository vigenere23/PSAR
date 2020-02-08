import yaml
import os

__script_dir = os.path.dirname(__file__)
__file_path = os.path.join(__script_dir, "./application.yml")

with open(__file_path, 'r') as __app_config_file:
  __app_config = yaml.safe_load(__app_config_file)

socketio_config = __app_config['socketio']
flask_config = __app_config['flask']

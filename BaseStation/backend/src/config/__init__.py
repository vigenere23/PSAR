import yaml
import os

__script_dir = os.path.dirname(__file__)
__file_path = os.path.join(__script_dir, "./application.yml")

with open(__file_path, 'r') as __app_config_file:
  app_config = yaml.safe_load(__app_config_file)

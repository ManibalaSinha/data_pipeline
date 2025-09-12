import yaml
from functools import lru_cache

@lru_cache()
def load_settings(path: str = "./configs/settings.yaml"):
   with open(path, "r") as f:
      return yaml.safe_load(f)
   

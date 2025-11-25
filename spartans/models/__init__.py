import os
import importlib
from django.db import models

# Dynamic model import
def import_models_dynamically():
    """Dynamically import all models from the models directory"""
    current_dir = os.path.dirname(__file__)
    model_files = [f[:-3] for f in os.listdir(current_dir) 
                   if f.endswith('.py') and f != '__init__.py']
    
    imported_models = {}
    for model_file in model_files:
        try:
            module = importlib.import_module(f'.{model_file}', package=__name__)
            # Get all model classes from the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, models.Model) and 
                    attr != models.Model):
                    imported_models[attr_name] = attr
                    globals()[attr_name] = attr
        except ImportError as e:
            print(f"Could not import {model_file}: {e}")
    
    return imported_models

# Import all models dynamically
import_models_dynamically()

# Explicit imports for backward compatibility
from .master_model import Category, Brand, BrandModel
from .product_model import product
from .service_model import Service, UserRequestService
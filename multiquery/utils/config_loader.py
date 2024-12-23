# File: multiquery/utils/config_loader.py

import yaml
import importlib

def load_config(file_path: str):
    """
    Loads the configuration file and returns it as a dictionary.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def instantiate_providers(config: dict):
    """
    Dynamically instantiates LLM providers based on the configuration.
    """
    providers = []
    for provider_config in config["llm_providers"]:
        # Dynamically import the provider class
        module_name, class_name = provider_config["class_path"].rsplit(".", 1)
        module = importlib.import_module(module_name)
        provider_class = getattr(module, class_name)

        # Instantiate the provider
        provider_instance = provider_class()  # Pass API key if required
        providers.append(provider_instance)
    return providers

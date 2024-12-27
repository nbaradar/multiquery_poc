# File: multiquery/main.py
import sys
import os
import argparse

# DEBUG: Print the Python path for debugging
print("Python path:", sys.path)

# I don't know why this is needed, but it is. It allows the import of the providers from the parent directory when running from VSCode "Play" button
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Don't know why this is needed either, but allows you to run from CLI
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from llm_providers.chatgpt import ChatGPTProvider
from llm_providers.grok import GrokProvider
from utils.config_loader import load_config, instantiate_providers

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query multiple LLM providers and display their responses.")
    parser.add_argument("query", type=str, nargs="?", help="The query to send to all LLM providers.")
    args = parser.parse_args()

    # If no prompt is provided, ask the user interactively
    if not args.query:
        print("No prompt arg provided. Please enter your query below:")
        args.query = input("")

    # Load configuration
    config = load_config("multiquery/config/config.yaml")

    # Instantiate providers
    providers = instantiate_providers(config)

    # Collect responses
    print("===== Multiquery Results =====\n")
    for provider in providers:
        response = provider.send_query(args.query)
        print(f"[{provider.__class__.__name__}]")
        print(response)
        print("\n==============================\n")

if __name__ == "__main__":
    main()

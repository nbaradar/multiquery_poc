# File: multiquery/main.py
import argparse
from llm_providers.chatgpt import ChatGPTProvider
from llm_providers.grok import GrokProvider
from multiquery.utils.config_loader import load_config, instantiate_providers
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query multiple LLM providers and display their responses.")
    parser.add_argument("query", type=str, help="The query to send to all LLM providers.")
    args = parser.parse_args()

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

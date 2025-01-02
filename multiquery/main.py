import sys
import os
import argparse
import asyncio
# I don't know why this is needed, but it is. It allows the import of the providers from the parent directory when running from VSCode "Play" button
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Don't know why this is needed either, but allows you to run from CLI
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from llm_providers.chatgpt import ChatGPTProvider
from llm_providers.grok import GrokProvider
from utils.config_loader import load_config, instantiate_providers
from utils.json_exporter import export_to_json
from utils.mongodb_client import store_result_in_mongodb

async def display_responses(results):
    """
    Displays the responses from the response.
    """
    # Collect and display responses
    # print("===== Multiquery Results =====\n")
    # for result in results:
    #     print(result.provider_name)
    #     if isinstance(result, Exception):
    #         print(f"Error: {result}")
    #     else:
    #         print(result)
    #     print("\n==============================\n")
    # Collect and display responses
    print("===== Multiquery Results =====\n")
    for provider, response in results.items():
        print(f"[{provider}]")
        if isinstance(response, Exception):
            print(f"Error: {response}")
        else:
            print(response)
        print("\n==============================\n")


async def run_providers_asynchronously(providers, query):
    """
    Runs the given providers using the provided query by the user. This is done asynchronously.

    :param providers: A list of provider instances. 
    :param query: The user query.
    """
    #Creates a list of tasks to be executed. In this case, each provider(task w/ async method) sends a query
    #.send_query does not get exected, but is turned into a coroutine object
    tasks = [provider.send_query(query) for provider in providers]

    # asyncio.gather takes the list of tasks and executes them concurrently.
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Loops through providers and results, zipping them together to create a dictionary of responses
    responses = {}
    for provider, result in zip(providers, results):
        provider_name = provider.provider_name
        if isinstance(result, Exception):
            responses[provider_name] = f"Error: {result}"
        else:
            responses[provider_name] = result

    return responses
    
async def main_async():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query multiple LLM providers and display their responses.")
    parser.add_argument("query", type=str, nargs="?", help="The query to send to all LLM providers.")
    parser.add_argument("--export-json", type=str, help="File path to save the query and responses in JSON format. If file already exists, it will append")
    args = parser.parse_args()

    # If no prompt is provided, ask the user interactively
    if not args.query:
        print("No prompt arg provided. Please enter your query below:")
        args.query = input("")

        print("Do you want to export the results?: (y/n): ", end="")
        export_choice = input("").strip().lower()
        if export_choice == 'y':
            args.export_json = input("Please enter the file path to save the results. Leave blank for default: ").strip()
        if args.export_json == "":
            args.export_json = "output/results.json"

    # Load configuration
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'config.yaml')
    config = load_config(config_path)

    # Instantiate providers
    # TL;DR Looking through the config file then dynamically creating provider instances based on the config
    providers = instantiate_providers(config)

    # Send query to all providers and return responses
    responses = await run_providers_asynchronously(providers, args.query)

    #Display responses
    await display_responses(responses)

    # Export results to JSON if requested
    if args.export_json:
        export_to_json(args.export_json, args.query, responses)
        print(f"\nResults exported to {args.export_json}")

    # Load MongoDB Config
    db_config = config.get("database", {})
    store_result_in_mongodb(
        uri=db_config.get("uri", "mongodb://localhost:27017"),
        db_name=db_config.get("name", "test"),
        collection_name=db_config.get("collection", "result"),
        data={
            "query": args.query,
            "responses": responses
        }
    )

if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except RuntimeError as e:
        if str(e) != "Event loop is closed":
            raise

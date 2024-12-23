# **Multiquery** &nbsp;![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Status](https://img.shields.io/badge/Status-POC-orange)

Multiquery is a **command-line application** written in Python designed to query multiple Large Language Models (LLMs) simultaneously from a single prompt.  
It currently supports **ChatGPT** and **Grok**, with the flexibility to add more LLM providers in the future.

---

## **Table of Contents**
1. [Features](#features)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Configuration](#configuration)
5. [Adding Providers](#adding-providers)
6. [Project Structure](#project-structure)
7. [Future Roadmap](#future-roadmap)

---

## **Features**

- **Single CLI Command**: Send the same query to all configured LLM providers with one command.
- **Clear Output**: Displays neatly formatted responses for each LLM side-by-side in the terminal.
- **Extensible Design**: Quickly add additional LLM providers by implementing a simple interface.
- **Config-Driven**: Set up your LLM providers in a YAML config file—no need to modify core code.
- **(Coming Soon)**: Progress bar for real-time status of query retrieval from each LLM.
- **(Coming Soon)**: Export queries and responses to **Markdown** in timestamped folders.

> **Note**  
> This is an early proof of concept (POC). Use it as a reference implementation or scaffold for your own multi-LLM projects.

---

## **Installation**

```bash
# Clone the repository
git clone https://github.com/your-username/multiquery.git

# Enter the project directory
cd multiquery

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> **Tip**  
> Python 3.8 or higher is recommended for this project.

---

## **Quick Start**

1. **Set up your YAML config** with your LLM API keys (see [Configuration](#configuration) below).
2. **Run the CLI** with a query:

   ```bash
   python -m multiquery.main "What is the capital of France?"
   ```

3. **See the results** from each configured LLM printed in the terminal:

   ```
   ===== Multiquery Results =====

   [ ChatGPTProvider ]
   Mock response from ChatGPT for query: What is the capital of France?

   [ GrokProvider ]
   Mock response from Grok for query: What is the capital of France?

   ================================
   ```

---

## **Configuration**

Multiquery uses a YAML configuration file (`config.yaml` by default) to set up each provider.  
Below is an example `config.yaml`:

```yaml
llm_providers:
  - name: chatgpt
    class_path: multiquery.llm_providers.chatgpt.ChatGPTProvider
    api_key: "YOUR_CHATGPT_KEY"

  - name: grok
    class_path: multiquery.llm_providers.grok.GrokProvider
    api_key: "YOUR_GROK_KEY"
```

- **`llm_providers`**: A list of providers you want to enable.
- **`name`**: A friendly name (not strictly used in code, but helpful for clarity).
- **`class_path`**: The import path to the provider’s class (for dynamic loading).
- **`api_key`**: Your API key or credential for that provider.

To use a custom config file:

```bash
python -m multiquery.main "Your question here" --config /path/to/another_config.yaml
```

> **Warning**  
> If your repository is public, avoid committing sensitive keys. Instead, use environment variables or a private config.

---

## **Future Roadmap**

Below are some upcoming features and design enhancements planned for Multiquery.  
Click to expand each section for more detail:

<details>
<summary><strong>Progress Bar</strong></summary>

### Progress Bar

We aim to integrate a progress bar for improved user feedback. When sending the query to multiple LLMs, a console-based progress bar (using libraries like [**tqdm**](https://github.com/tqdm/tqdm) or [**rich**](https://github.com/Textualize/rich)) will show how many of the providers have returned responses.

- **Parallel Requests?**  
  Eventually, we’d also like to handle requests concurrently so that each LLM can be queried in parallel rather than sequentially.

</details>

<details>
<summary><strong>Export to Markdown</strong></summary>

### Export Queries & Responses to Markdown

A feature to export your prompt and all LLM responses into a timestamped folder. This will:
1. Create a folder named with the date/time.
2. Save the prompt in `prompt.md`.
3. Save each LLM’s response in a separate file, e.g. `ChatGPTProvider_response.md`.

```bash
exports/
└─ multiquery_20241223_153045/
   ├─ prompt.md
   ├─ ChatGPTProvider_response.md
   └─ GrokProvider_response.md
```

This makes it easy to review, share, or archive your results.
</details>

---

**Enjoy using Multiquery!** If you have any questions, suggestions, or run into issues, please open an [Issue](https://github.com/your-username/multiquery/issues) or submit a Pull Request. Together, we can make multi-LLM querying simpler and more powerful.

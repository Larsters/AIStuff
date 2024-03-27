# Creative LLM Poet

## Overview

Creative LLM Poet is an innovative application designed to blend the art of poetry with the cutting-edge capabilities of Large Language Models (LLMs). It specializes in generating small poems in the style of Kanye West, based on user-provided topics. This project not only showcases the creativity possible through LLMs but also demonstrates practical uses of LangChain tools for dynamic content creation.

Features include:
- **Poem Generation:** Generates poems based on specified topics, mimicking the unique style of Kanye West.
- **Interactive Tools:** Utilizes custom-built LangChain tools for text analysis, including text length calculation.
- **LLM Integration:** Incorporates LangChain with OpenAI's ChatGPT for sophisticated text processing and summarization.

This project serves as a practical example of how LangChain agents and OpenAI's APIs can be orchestrated to produce creative content and perform textual analyses.

## Installation

Ensure you have Python and pipenv on your system. Set up your project environment with these steps:

1. **Environment Setup:**

   Create and activate a virtual environment:

   ```bash
   pipenv install
   pipenv shell
   pipenv install langchain openai black python-dotenv
   ```

**You must provide your own API keys.** Add these keys to a `.env` file in the project directory. For example:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
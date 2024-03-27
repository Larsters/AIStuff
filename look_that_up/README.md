# Do Look Up

## Overview

Do Look Up simplifies the process of finding detailed information about individuals online. It combines modern web technologies to offer a streamlined approach to data retrieval and analysis:

- **Efficient Online Searches:** Leverages SerpAPI for direct search results, avoiding the complexity of web scraping.
- **LinkedIn Insights:** Gathers comprehensive LinkedIn profiles through Proxycurl, providing more detailed information than typical scraping methods.
- **Summarization and Insight:** Utilizes the ChatGPT 3.5 Turbo API to summarize data, highlighting only the most relevant information in an understandable summary.

This project offers a hands-on experience with LangChain agents for fetching and summarizing LinkedIn profiles, making it an ideal exploration for technology enthusiasts.

## Installation

Ensure Python and pipenv are installed. Follow these steps to prepare your environment:

1. **Environment Setup:**

   Initialize and activate a virtual environment:

   ```bash
   pipenv install
   pipenv shell
   pipenv install langchain openai black python-dotenv
   ```

**You must provide your own API keys.** Add these keys to a `.env` file in the project directory. For example:

```bash
OPENAI_API_KEY=your_openai_api_key_here
PROXYCURL_API_KEY=your_proxycurl_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```
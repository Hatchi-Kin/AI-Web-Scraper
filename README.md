# AI Web Scraper

This project is an AI-powered web scraper that uses Selenium, BeautifulSoup, and LangChain to scrape and parse web content.


## Pre-requisites

- Ollama needs to be installed, the code uses llama3.2
- chrome driver can be downloaded from https://googlechromelabs.github.io/chrome-for-testing/#stable
- and a auth token can be obtained from Bright Data and set in the .env file

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/ai-web-scraper.git
    cd ai-web-scraper
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Copy `example.env` to `.env` and update the `SBR_WEBDRIVER` value with your WebDriver URL.

## Usage

1. **Run the Streamlit app:**
    ```sh
    streamlit run main.py
    ```

2. **Open the app in your browser:**
    - Local URL: `http://localhost:8501`
    - Network URL: `http://<your-ip>:8501`

3. **Scrape a website:**
    - Enter the website URL in the input field and click "Scrape Website".

4. **Parse the content:**
    - Describe what you want to parse in the text area and click "Parse Content".

## Dependencies

- Streamlit
- LangChain
- LangChain Ollama
- Selenium
- BeautifulSoup4
- lxml
- html5lib
- python-dotenv
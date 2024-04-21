# Text-to-Speech (TTS) Automation

![Script in Action](https://github.com/AnubhavChaturved1/British-Brian-TTS/blob/main/Screenshot%202024-04-13%20160030.png)


This Python script automates the process of converting text to speech using a web-based TTS service. It utilizes Selenium WebDriver to interact with the website.

## Setup

1. Install Python if not already installed.
2. Install required Python packages using pip:
    ```
    pip install selenium webdriver-manager
    ```
3. Ensure Google Chrome is installed on your system.
4. Install ChromeDriver using WebDriverManager:
    ```python
    from webdriver_manager.chrome import ChromeDriverManager
    
    # Install ChromeDriver binary
    ChromeDriverManager().install()
    ```

## Usage

1. Clone the repository or download the script.
2. Run the script with Python.
    ```
    python tts_automation.py
    ```
3. Input text when prompted.
4. The script will navigate to the TTS website, input the text, generate speech, and play the speech audio.

## Dependencies

- Python 3.11.4
- Selenium WebDriver
- WebDriverManager
- Google Chrome

## Configuration

- `--headless`: Runs Chrome in headless mode (without opening a browser window).
- `--log-level=3`: Sets the log level to suppress console logs.
- `--disable-blink-features=AutomationControlled`: Disables Blink features to avoid detection by websites.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


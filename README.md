# Amazon Bot

This repository contains a simple Python script that uses Selenium to open a headless Chrome browser and log in to Amazon.com.

## Requirements
- Python 3.12+
- `selenium` package
- ChromeDriver installed and accessible via PATH

Install dependencies with:

```bash
pip install selenium
```

Ensure ChromeDriver is available in your system PATH. You can download it from [ChromeDriver documentation](https://chromedriver.chromium.org/).

## Usage
Set your Amazon credentials as environment variables `AMAZON_EMAIL` and `AMAZON_PASSWORD` and run the script:

```bash
export AMAZON_EMAIL="your-email@example.com"
export AMAZON_PASSWORD="your-password"
python3 amazon_bot.py
```

**Warning**: Do not commit your credentials or share them publicly. The script may require additional manual steps for multi-factor authentication or CAPTCHA challenges on Amazon's login page.

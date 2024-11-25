BTC Price Tracker: A Python application using tkinter for the UI and requests to fetch live Bitcoin prices

BTC Price Tracker
Overview

The BTC Price Tracker is a Python application that provides the current Bitcoin (BTC) price using a sleek graphical interface built with tkinter. The app fetches real-time BTC price data via the CoinRanking API and displays it on a dark-themed user interface.
Features

    Live Bitcoin Price: Retrieves the latest Bitcoin price in USD.
    User-Friendly Interface: Minimalistic design with a modern dark purple theme.
    One-Click Fetch: Simply click the button to get the latest BTC price.
    API Integration: Uses the CoinRanking API for real-time price data.

Requirements

    Python 3.x
    Libraries:
        tkinter (comes pre-installed with Python).
        requests (install via pip install requests).
    API Key for CoinRanking (modify the x-rapidapi-key value in the code).

How It Works

    Fetch Price:
        The app sends a request to the CoinRanking API.
        Retrieves the current Bitcoin price in USD.
    Display Price:
        Updates the UI with the fetched price.

Installation

    Clone or download this repository.
    Install the required libraries:

pip install requests

Run the script:

    python btc_price_tracker.py

Usage

    Open the application.
    Click the "Get BTC Price" button to fetch the current Bitcoin price.

Example Execution
Initial Screen:

    Displays the message: "Click the button to get BTC price."

After Clicking the Button:

    Displays: BTC Price: <latest_price>$

API Information

    Base URL: https://coinranking1.p.rapidapi.com/
    Endpoint Used: /coin/Qwsogvtv82FCd/price
    API Key: Replace "x-rapidapi-key" in the code with your CoinRanking API key.

Design Highlights

    Dark Theme:
        Background: #1D1B2A (dark purple).
        Label Text: Yellow for high visibility.
        Button: Purple shade (#5D3A5A) with white text.

Customization

    Modify the API endpoint or parameters to fetch data for other cryptocurrencies.
    Adjust the design by changing the colors in the screen.config() or button/label settings.

File Structure

    btc_price_tracker.py: Main script for the application.

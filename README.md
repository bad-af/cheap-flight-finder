# Cheap Flight Finder

A Python program that helps find cheap travel destinations from Portugal — without having to pick a destination first.

## Motivation

I'm a student and travel on a limited budget. Often what matters most isn't going to one specific place, it's being able to travel within what I can actually afford. Instead of picking a destination and then finding out the flights are out of reach, this program works the other way around: it tells me which destinations actually fit my budget, within a chosen date window.

I started this project mainly to learn Python by building something real, rather than only working through isolated exercises.

## How it works

The user provides:
- Maximum budget (€)
- Travel date window (start and end date)
- Minimum and maximum trip duration (days)

The program searches round-trip flights from several Portuguese airports to a set of European destinations, and returns the destinations whose cheapest found flight falls within budget, sorted from cheapest to most expensive.

## Current limitations (V1)

- **Data is not a live search.** Prices come from the [Travelpayouts Data API](https://travelpayouts.com), which returns the cheapest price *recently found by other users* (cached, up to 48h), not a real-time search across all airlines. It's a discovery tool, not a guaranteed booking price.
- **Fixed trip duration.** Only the minimum duration entered is currently tested, not the full range between minimum and maximum.
- **Limited airport and destination list.** Covers 5 Portuguese airports and around 23 European destinations with frequent low-cost routes — not yet a search across all of Europe.
- **No network error handling.** If the API is unavailable or returns an error, the program doesn't yet handle that case gracefully.

## Running locally

1. Clone the repository and install dependencies:
```bash
   pip install -r requirements.txt
```
2. Create a `.env` file in the project root with your Travelpayouts key:
3. Run the program:
```bash
   python main.py
```

## Technologies

- Python
- [requests](https://docs.python-requests.org/) — HTTP requests to the API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — API key management
- [Travelpayouts Data API](https://travelpayouts.com) — flight price data

## Possible future versions

- Compare prices against historical averages to better highlight good deals
- Test all durations between the minimum and maximum entered, not just the minimum
- Periodic alerts when an especially good deal appears
- Wider list of European airports and destinations
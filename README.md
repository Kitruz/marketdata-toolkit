# marketdata-toolkit
A Python-based backtesting engine that pulls historical data, calcualates indicators, generates buy/sell signal, and si,ulates a portfolio to test trading strategies.

## What it does
- Scrapes data for given ticker using yfinance libary
- Calculates given indicators
- Generates buy/sell signal
- Simulates a portfolio (cash, shares, book_value) day-by-day through historical data
- Plots price, indicators, and signals to visually verify results

## Know problems
- Need to find solution to "dead zone", wheras since you only scraped data of a given period.
  If you calculate MA200 it wont pick up till after 200 days.
- Single ticker only - multi-ticker WIP
- RSI is calculated but implementation of buy/sell signal WIP

## Roadmap
1. Multiple ticker support
2.  Build strategy abstraction, strategy interface, and make rules configurable instead of hard-coded. 
3. Implement Realistic Trade Simulation
    - Track cash, positions, cost basis, realized, portfolio value.
    - Transactions cost or FX Risk, and slippage assumptions.
    - Rid of buy one share logic; use position sizing.
4. Add Evaluation Metrics
    - Compute total return, drawdown, and risk-adjusted metric
    - Store results in object rather print statements


# marketdata-toolkit
A Python-based backtesting engine that pulls historical data, calculates indicators, generates buy/sell signal, and simulates a portfolio to test trading strategies.

## What it does
- Scrapes data for given ticker using yfinance libary
- Calculates given indicators
- Generates buy/sell signal
- Simulates a portfolio (cash, shares, book_value) day-by-day through historical data
- Plots price, indicators, and signals to visually verify results

## Roadmap
1. Working on implementing OOP architecture, separating intent and state between objects. Finish first rough version. 
2. Add Evaluation Metrics to evaluate portfolio performance. 
    - Return total return, risk-adjusted, sharpe.
3. Work on data pipeline, make sure data is accurate and reliable. 
3. Implement realistic accounting
    - Add FX, fees, slippage between order and execution. 

# Ideas
- Strategy Report: 1. Period (Trading Start Date, End Date, and Perpiod Run)
                   2. Metrics (Starting Capital, Final Equity, Total Return, SPY Benchmark
                               CAGR, Win Rate, Biggest Win/Loss, Average P&L, Avg Holding Time, Max Drawdown, Sharpe Ratio)
                   3. Trades (Total, Long, Short)
- Add scores or confidence to strategies based off evaluation.
- Evenutally utilize an optimization algo to develop strategies through multiple simulations; genetic algo and ML.
- Implement Dashboard for better commuicate results and model.
- Implement Screener. 

# Implemented
- Multi ticker support

import yfinance as yf
import pandas as pd

# Pull data
def pull_data(ticker_symbol, period = "2y"):
    '''
    purpose: get raw historical price data from one ticker from yfinance
    parameter: ticker_symbol (str) - e.g. "AAPL". period (str) - e.g. "2y".
    return: hist (DataFrame) - daily price data, indexed by date. 
    '''
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period = period)
    hist = hist.dropna(subset = ['Close'])

    return hist


# Indicators
def calculate_indicators(hist):
    '''
    purpose: add moving average (MA) columns to the price data.
    parameters: hist (DataFrame) - must contain a 'Close' column.
    return: hist (DataFrame) - same data, with MA50 and MA200 columns added. 
    '''
    hist['MA50'] = hist['Close'].rolling(50).mean()
    hist['MA200'] = hist['Close'].rolling(200).mean()

    return hist

# Signals 
def generate_signals(hist):
    '''
    purpose: decide which days count as buy or sell, based on indicators.
    parameters: hist (DataFrame) - must contain MA50 and MA 200 columns.
    return: hist (DataFrame) - same data, with buy_signal and sell_signal columns added. 
    '''
    hist['buy_signal'] = (hist['MA50'] > hist['MA200']) & (hist['MA50'].shift(1) <= hist['MA200'].shift(1))
    hist['sell_signal'] = (hist['MA50'] < hist['MA200']) & (hist['MA50'].shift(1) >= hist['MA200'].shift(1))

    return hist

# Engine skeleton
def run_backtest(hist, initial_cash = 1000, buy_pct = 0.25):
    '''
    purpose: walk through data day by day, simulating buys and sells.
    parameters: hist(DataFrame) - must contain buy_signal and sell_signal columns. 
                intial_cash(float) - starting cash. buy_pct(float) - percentage of cash to spend on each buy.
    return: cash(float), shares(float), book_value(float) - ending state after the full simulation.
    '''
    cash = initial_cash
    shares = 0
    book_value = 0

    for date, row in hist.iterrows():
        price = row['Close']

        if row['buy_signal'] and cash > 0:
            spend = cash * buy_pct
            shares += spend / price
            cash -= spend
            book_value += spend
            print(date, "BUY", round(spend, 2), "cash left:", round (cash, 2))

        elif row['sell_signal'] and shares > 0:
            proceeds = shares * price
            realized_value = proceeds - book_value
            cash += proceeds
            shares = 0
            book_value = 0
            print(date, "SELL", "cash now", round(cash, 2), "realized gain/loss:", round(realized_value, 2))

    return cash, shares, book_value

# Summarize Results
def summarize_results(hist, cash, shares, book_value, initial_cash):
    '''
    purpose: turn ending cash/shares/book_value into readable results.
    parameters: hist(DataFrame), cash(float), shares(float), book_value(float), initial_cash(float)
    return: None - this function only prints
    '''
    final_price = hist['Close'].iloc[-1]
    current_value_of_holdings = shares * final_price
    portfolio_value = cash + current_value_of_holdings
    overall_return = (portfolio_value - initial_cash) / initial_cash

    print("\n--- Summary ---")
    print(f"Available cash: ${cash:,.2f}")
    print(f"Current value of holdings: ${current_value_of_holdings:,.2f}")

    if shares > 0:
        holding_return = (current_value_of_holdings - book_value) / book_value
        holding_gain_loss = current_value_of_holdings - book_value

        print(f"Book Value (cost basis) of holdings: ${book_value:,.2f}")
        print(f"Return on holdings: {holding_return:.2%}")
        print(f"Gain/loss on holdings: ${holding_gain_loss:,.2f}")

    print(f"Total portfolio value: ${portfolio_value:,.2f}")
    print(f"Overall return (start to end): {overall_return:.2%}")


# Main function
def run_engine():
    '''
    '''
    hist = pull_data("AAPL")
    hist = calculate_indicators(hist)
    hist = generate_signals(hist)
    cash, shares, book_value = run_backtest(hist)
    summarize_results(hist, cash, shares, book_value, initial_cash = 1000)

# actually runs the main function
run_engine()
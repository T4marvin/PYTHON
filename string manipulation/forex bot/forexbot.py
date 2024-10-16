import MetaTrader5 as mt5

# Initialize the MetaTrader 5 connection
if not mt5.initialize():
    print("Initialization failed")
    mt5.shutdown()

# Log in to your account
account = 12345678
password = "your_password"
server = "your_server"

if not mt5.login(account, password=password, server=server):
    print("Login failed")
    mt5.shutdown()

import pandas as pd

# Define the symbol and timeframe
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H1
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1000)

# Convert to DataFrame
rates_frame = pd.DataFrame(rates)
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
print(rates_frame.head())

# Calculate moving averages
rates_frame['SMA_50'] = rates_frame['close'].rolling(window=50).mean()
rates_frame['SMA_200'] = rates_frame['close'].rolling(window=200).mean()

# Generate signals
rates_frame['signal'] = 0
rates_frame['signal'][50:] = np.where(rates_frame['SMA_50'][50:] > rates_frame['SMA_200'][50:], 1, 0)
rates_frame['position'] = rates_frame['signal'].diff()

print(rates_frame[['time', 'close', 'SMA_50', 'SMA_200', 'signal', 'position']].tail())

for i in range(len(rates_frame)):
    if rates_frame['position'][i] == 1:
        # Buy signal
        mt5.order_send(symbol=symbol, action=mt5.TRADE_ACTION_DEAL, type=mt5.ORDER_TYPE_BUY, volume=0.1, price=mt5.symbol_info_tick(symbol).ask)
    elif rates_frame['position'][i] == -1:
        # Sell signal
        mt5.order_send(symbol=symbol, action=mt5.TRADE_ACTION_DEAL, type=mt5.ORDER_TYPE_SELL, volume=0.1, price=mt5.symbol_info_tick(symbol).bid)

mt5.shutdown()

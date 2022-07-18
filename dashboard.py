import yfinance 
import mplfinance 

ticker = "TSLA"
history = yfinance.Ticker(ticker).history(period="3mo")
print(f"3 months low: {history.Low.min().astype(int)}")
print(f"3 months high: {history.High.max().astype(int)}")
history.tail() 
mplfinance.plot(history,type='candle',mav=(7),figratio=(18,10))
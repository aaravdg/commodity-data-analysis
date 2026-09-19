import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("Downloading Brent Crude and WTI Crude market data...")
brent = yf.download('BZ=F', start='2023-01-01', end='2026-09-01')['Close']
wti = yf.download('CL=F', start='2023-01-01', end='2026-09-01')['Close']

df = pd.concat([brent, wti], axis=1).dropna()
df.columns = ['Brent', 'WTI']
df['Spread'] = df['Brent'] - df['WTI']
df['30MA'] = df['Spread'].rolling(window=30).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Spread'], label='Brent - WTI Spread ($/bbl)', color='#1f77b4', alpha=0.7)
plt.plot(df.index, df['30MA'], label='30-Day Moving Average', color='#ff7f0e', linewidth=2)
plt.title('Historical Brent vs. WTI Crude Oil Price Differential')
plt.xlabel('Date')
plt.ylabel('Spread (USD per Barrel)')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('brent_wti_spread.png', dpi=300)
print("Success! Analysis complete. Chart saved as 'brent_wti_spread.png'.")

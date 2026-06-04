import pandas as pd

trades = pd.DataFrame({
    "TradeID":[1,2,3],
    "Trader":["A","B","C"],
    "Amount":[100000,250000,175000]
})

trades.to_csv("processed_trades.csv", index=False)
print("ETL Pipeline Completed")

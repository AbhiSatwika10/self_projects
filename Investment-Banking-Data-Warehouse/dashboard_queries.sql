SELECT trader, SUM(amount)
FROM trades
GROUP BY trader;

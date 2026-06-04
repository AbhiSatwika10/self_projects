import numpy as np

def calculate_var(returns, confidence=0.95):
    percentile = np.percentile(returns, (1-confidence)*100)
    return abs(percentile)

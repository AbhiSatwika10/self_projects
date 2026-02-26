def evaluate_risk(match, blink):

    risk = "LOW"

    if not blink:
        risk = "HIGH"

    if match and blink:
        status = "ACCESS_GRANTED"
    else:
        status = "ACCESS_DENIED"

    return status, risk

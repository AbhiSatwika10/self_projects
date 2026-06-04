import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "income":[50000,60000,20000,100000],
    "loan":[10000,15000,5000,20000],
    "default":[0,0,1,0]
})

X = data[["income","loan"]]
y = data["default"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,pred))

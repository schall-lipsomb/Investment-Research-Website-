from sklearn.tree import DecisionTreeClassifier

# Hand-labeled training examples: [debt_to_equity, revenue_growth] -> risk label
# revenue_growth is a decimal (0.10 = 10%), matching what yfinance returns
TRAINING_DATA = [
    # Low risk: low debt, healthy growth
    ([20, 0.15], "Low"),
    ([30, 0.10], "Low"),
    ([15, 0.20], "Low"),
    ([40, 0.08], "Low"),
    ([25, 0.12], "Low"),

    # Medium risk: moderate debt or slow/flat growth
    ([80, 0.05], "Medium"),
    ([90, 0.03], "Medium"),
    ([70, 0.02], "Medium"),
    ([100, 0.04], "Medium"),
    ([60, 0.01], "Medium"),

    # High risk: high debt or shrinking revenue
    ([150, -0.05], "High"),
    ([200, 0.00], "High"),
    ([180, -0.10], "High"),
    ([250, 0.02], "High"),
    ([160, -0.02], "High"),
]

X_train = [features for features, label in TRAINING_DATA]
y_train = [label for features, label in TRAINING_DATA]

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)


def predict_risk(debt_to_equity, revenue_growth):
    if debt_to_equity is None or revenue_growth is None:
        return "Unknown"
    prediction = model.predict([[debt_to_equity, revenue_growth]])
    return prediction[0]

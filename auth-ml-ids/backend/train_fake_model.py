from sklearn.ensemble import RandomForestClassifier
import joblib

# Modelo simples com 1 entrada e 1 saída
X = [[0, 0, 0]]
y = ["normal"]

model = RandomForestClassifier()
model.fit(X, y)

# Salva modelo como .pkl
joblib.dump(model, "backend/modelo_ml.pkl")
print("[+] Modelo fake salvo em backend/modelo_ml.pkl")

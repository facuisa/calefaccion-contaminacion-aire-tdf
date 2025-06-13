# src/models/training.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def entrenar_modelos(df_total):
    # Separar variables predictoras y objetivo
    X = df_total.drop(columns=['Riesgo'])
    y = df_total['Riesgo']

    # Codificar etiquetas
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Dividir datos en entrenamiento y testeo
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded)

    # Entrenar Árbol de Decisión
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)
    y_pred_dt = dt.predict(X_test)
    acc_dt = accuracy_score(y_test, y_pred_dt)

    # Entrenar Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    conf_rf = confusion_matrix(y_test, y_pred_rf)

    return dt, rf, {
        "accuracy_dt": acc_dt,
        "accuracy_rf": acc_rf,
        "confusion_rf": conf_rf,
        "label_encoder": le,
        "y_test": y_test,
        "y_pred_rf": y_pred_rf
    }
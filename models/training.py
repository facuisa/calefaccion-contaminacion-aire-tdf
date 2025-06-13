# src/models/training.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def entrenar_modelos(df):
    # Separar variables predictoras (X) y variable objetivo (y)
    X = df.drop(columns=['Riesgo'])
    y = df['Riesgo']

    # Codificar etiquetas
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # División en entrenamiento y test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    # Modelos
    dt = DecisionTreeClassifier(random_state=42)
    rf = RandomForestClassifier(random_state=42)

    # Entrenamiento
    dt.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    # Predicción
    y_pred_rf = rf.predict(X_test)

    # Métricas
    accuracy_dt = accuracy_score(y_test, dt.predict(X_test))
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    confusion_rf = confusion_matrix(y_test, y_pred_rf)

    return dt, rf, {
        'accuracy_dt': accuracy_dt,
        'accuracy_rf': accuracy_rf,
        'confusion_rf': confusion_rf,
        'label_encoder': le,
        'y_test': y_test,               # <- ESTOS SON LOS CLAVES
        'y_pred_rf': y_pred_rf          # <- PARA QUE FUNCIONE EL SIGUIENTE BLOQUE
    }
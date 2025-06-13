# src/models/training.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def entrenar_modelos(df, variable_objetivo='Riesgo', test_size=0.2, random_state=42):
    """
    Entrena y evalúa Decision Tree y Random Forest con GridSearchCV.
    Retorna los modelos entrenados y un diccionario con los resultados.
    """
    
    # Separar X e y
    X = df.drop(columns=[variable_objetivo, 'PM10'])  # Evitamos data leakage
    y = df[variable_objetivo]

    # Codificar etiquetas
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Dividir en train y test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=random_state, stratify=y_encoded
    )

    # Escalado robusto
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- Decision Tree ---
    param_grid_dt = {
        'max_depth': [None, 5, 10, 15],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'criterion': ['gini', 'entropy']
    }

    dt = DecisionTreeClassifier(random_state=random_state)
    grid_dt = GridSearchCV(dt, param_grid_dt, cv=5, scoring='f1_weighted', n_jobs=-1)
    grid_dt.fit(X_train_scaled, y_train)

    y_pred_dt = grid_dt.predict(X_test_scaled)
    report_dt = classification_report(y_test, y_pred_dt, target_names=le.classes_, output_dict=True)

    # --- Random Forest ---
    param_grid_rf = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'criterion': ['gini']
    }

    rf = RandomForestClassifier(random_state=random_state)
    grid_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='f1_weighted', n_jobs=-1)
    grid_rf.fit(X_train_scaled, y_train)

    y_pred_rf = grid_rf.predict(X_test_scaled)
    report_rf = classification_report(y_test, y_pred_rf, target_names=le.classes_, output_dict=True)

    return grid_dt.best_estimator_, grid_rf.best_estimator_, {
        'label_encoder': le,
        'report_dt': report_dt,
        'report_rf': report_rf,
        'confusion_dt': confusion_matrix(y_test, y_pred_dt),
        'confusion_rf': confusion_matrix(y_test, y_pred_rf),
        'accuracy_dt': report_dt['accuracy'],
        'accuracy_rf': report_rf['accuracy']
    }
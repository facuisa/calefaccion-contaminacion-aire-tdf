# src/models/train_model.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def preparar_datos(df, target='Riesgo', drop_cols=['PM10']):
    df = df.copy()
    X = df.drop(columns=[target] + drop_cols)
    y = df[target]
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    return X, y_encoded, le

def escalar_datos(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test

def entrenar_gridsearch(modelo, param_grid, X_train, y_train, cv=5):
    grid = GridSearchCV(estimator=modelo, param_grid=param_grid, cv=cv,
                        scoring='f1_weighted', n_jobs=-1)
    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_, grid.best_score_

def evaluar_modelo(modelo, X_test, y_test, le, titulo=''):
    y_pred = modelo.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=le.classes_, yticklabels=le.classes_, cmap='Blues')
    plt.xlabel("Predicción")
    plt.ylabel("Real")
    plt.title(f"Matriz de Confusión - {titulo}")
    plt.tight_layout()
    plt.show()
    
    return report, cm

def comparar_modelos(report_dt, report_rf):
    print("Comparación Resumida:")
    print("Métrica        | Árbol Decisión | Random Forest")
    print("-----------------------------------------------")
    print(f"Accuracy       | {report_dt['accuracy']:.2f}            | {report_rf['accuracy']:.2f}")
    print(f"F1-score (Alto) | {report_dt['Alto']['f1-score']:.2f}            | {report_rf['Alto']['f1-score']:.2f}")
    print(f"F1-score (Medio)| {report_dt['Medio']['f1-score']:.2f}            | {report_rf['Medio']['f1-score']:.2f}")
    print(f"F1-score (Bajo) | {report_dt['Bajo']['f1-score']:.2f}            | {report_rf['Bajo']['f1-score']:.2f}")
    print(f"F1-score (Promedio Ponderado)| {report_dt['weighted avg']['f1-score']:.2f} | {report_rf['weighted avg']['f1-score']:.2f}")

    if report_rf['weighted avg']['f1-score'] > report_dt['weighted avg']['f1-score']:
        print("\nRandom Forest tuvo un mejor rendimiento global.")
    elif report_rf['weighted avg']['f1-score'] < report_dt['weighted avg']['f1-score']:
        print("\nÁrbol de Decisión tuvo un mejor rendimiento global.")
    else:
        print("\nAmbos modelos tienen un rendimiento similar.")

    if report_rf['Alto']['f1-score'] > report_dt['Alto']['f1-score']:
        print("Random Forest también rindió mejor en la clase de riesgo 'Alto'.")
    elif report_rf['Alto']['f1-score'] < report_dt['Alto']['f1-score']:
        print("Árbol de Decisión rindió mejor en la clase de riesgo 'Alto'.")
    else:
        print("Ambos modelos tuvieron un desempeño similar en la clase de riesgo 'Alto'.")
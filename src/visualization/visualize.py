# src/visualization/visualize.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, figsize=(15, 10), bins=30):
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    numeric_cols.hist(figsize=figsize, bins=bins)
    plt.suptitle('Distribución de Variables Numéricas', y=1.02)
    plt.tight_layout()
    plt.show()

def plot_boxplots_vs_riesgo(df, variables_clave, riesgo_col='Riesgo'):
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(variables_clave):
        plt.subplot(2, 3, i + 1)
        sns.boxplot(x=riesgo_col, y=col, data=df, order=['Bajo', 'Medio', 'Alto'])
        plt.title(f'Distribución de {col} por Nivel de Riesgo')
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlación entre Variables Numéricas')
    plt.tight_layout()
    plt.show()

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('cases-brazil-total.csv')
print("Colunas do DataFrame:", df.columns)
col_name = 'state'
cases_col = 'totalCases'
data_x = df[col_name].tolist()
data_y = df[cases_col].tolist()
title = 'Total de Casos de COVID-19 por Estado'
x_label = 'Estado'
y_label = 'Total de Casos'
plt.figure(figsize=(14, 8))
ax = sns.barplot(x=data_x, y=data_y, color='blue')
ax.set_title(title, fontsize=16, weight='bold')
ax.set_xlabel(x_label, fontsize=14)
ax.set_ylabel(y_label, fontsize=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=12)
output_dir = 'gráficos'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'total_cases_by_state.png')
figure = ax.get_figure()
figure.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close(figure)
print(f"\nGráfico foi salvo em:\n{output_file}\n")
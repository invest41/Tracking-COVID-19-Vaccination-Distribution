import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


df = pd.read_csv('/content/vaccine_data.csv', index_col='date',parse_dates=True,error_bad_lines=False)
print(list(df.columns))

#column chart
plt.figure(figsize=(40,20))
sns.barplot(x=df['country'],y=df['daily_vaccinations'])

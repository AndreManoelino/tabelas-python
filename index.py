import pandas as pd 
input_file_path =   r'C:\xampp\htdocs\supermarket_sales - Sheet1.csv'

try: 
    df = pd.read_csv(input_file_path)
except   FileNotFoundError:
    print(f"o arquivo csv não foi encontraado em :{input_file_path}")
    exit()

df.rename(columns={
    'Invoice Id': 'Id da Fatura',
    'Branch': 'Filial',
    'City': 'Cidade',
    'Gross incone': 'Renda bruta',
    'Rating': 'Avaliação'
}, inplace=True)    
df['Resultado'] = '+1' 
df = df.applymap(lambda x: x +10 if isinstance(x, (int, float)) else x )
print (df) 

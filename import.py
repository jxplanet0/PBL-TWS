import pandas as pd
df = pd.read_excel("C:/Users/BAGAS/Downloads/laptop.xlsx") # Rubah ini
df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:Dynamic01:@localhost:5432/pbl-tws') # Rubah ini 

df.to_sql("laptop", engine)
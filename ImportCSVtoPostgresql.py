import pandas as pd
gd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/Datasets/Geweldsdelicten.csv', sep=';')
fd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/Datasets/Fietsendiefstal.csv', sep=';')
gd.columns = [c.lower() for c in gd.columns] #postgres doesn't like capitals or spaces
fd.columns = [c.lower() for c in fd.columns] #postgres doesn't like capitals or spaces


from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:pgadmin2017@localhost:5432/StekOverflow')

gd.to_sql("geweldsdelicten", engine)
fd.to_sql("fietsendiefstal", engine)


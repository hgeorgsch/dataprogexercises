import pandas as pd 
df = pd.read_csv("studenter-bb.xls", encoding="UTF-16", header=0, sep='\t')
df_moodle = df.rename(columns={
    'Etternavn': 'lastname',
    'Fornavn': 'firstname',
    'Brukernavn': 'username',
    'Student-ID': 'idnumber'
})
df_moodle = df_moodle.drop(columns=["Unnamed: 4"])
df_moodle.insert(4, 'email', [f"{u}@stud.ntnu.no" for u in df_moodle["username"].values])
df_moodle.to_csv("studenter-moodle.xls", index=False)

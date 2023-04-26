import pandas as pd
import datetime 
import numpy as np

marathon = pd.read_csv("https://raw.githubusercontent.com/pesikj/PythonProDataScience/09dd5db1d5b617c624718d18f7fc6afc33699394/03/half_marathon.csv")

marathon = marathon.iloc[:, [0, 2, 1]]
marathon.sort_values(by= ["Jmeno", "Rok zavodu"], inplace = True)


marathon["Cas zavodnika"] = pd.to_datetime(marathon["Cas zavodnika"], 
                                           format= '%H:%M:%S', cache=False )#.dt.time - vrati zpet na objekt
marathon.dtypes
marathon_copy = marathon[:]

marathon["cas 2020"] = marathon.groupby("Jmeno")["Cas zavodnika"].shift(-1)
# marathon[marathon["Jmeno"].isin(["Vacek Martin", "Půta Roman", "Zeman Martin"])] #co udela shift s duplicity

marathon.dropna(inplace = True)

marathon["diff"] = marathon["cas 2020"] -marathon["Cas zavodnika"]

marathon["diff"] = marathon["diff"].dt.total_seconds()

marathon["zaver"] = np.where(marathon["diff"]>0, "zpomalil/la", "zrychlil/la")
marathon.groupby("zaver")["Jmeno"].count()
marathon.groupby("zaver")["diff"].mean()#.apply(lambda x: x.mean()/60) # prumer v minutach - apply v pristi lekce

################### Nesrovnalosti v datech
small_set = marathon_copy.loc[marathon_copy["Jmeno"].str.startswith("Ba")]
small_set.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")
marathon_copy.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")# error - duplicity
#Vacek Martin bezel 3x. Mozna to je otec a syn
bezci = marathon_copy.groupby("Jmeno", as_index=False).count()
bezci.loc[bezci["Cas zavodnika"]>2, :]
marathon_copy.loc[marathon_copy["Jmeno"]=="Vacek Martin"]

# 3 zavodnici bezeli vic nez jednou v roce. Nejspis jsou to ruzne lidi se stejnym jmenem

bezci = marathon_copy.groupby(["Jmeno", "Rok zavodu"], as_index=False).count()
bezci.loc[bezci["Cas zavodnika"]>1, :]

# Muzeme but vycistit duplicity, nebo pridat rozlisovaci priznak
# vycistime duplicity

marathon_no_dupl = marathon_copy[~marathon_copy["Jmeno"].isin(["Vacek Martin", "Půta Roman", "Zeman Martin"])]

#ted muzeme vytvorit kontingencni tabulku
marathon_pivot = marathon_no_dupl.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")

#zopakujeme analyzu casu, tentokrat na vytvorene pivot tabulce

marathon_pivot.dropna(inplace = True)
marathon_pivot["diff"] = marathon_pivot[2020] -marathon_pivot[2019]
marathon_pivot["diff"] = marathon_pivot["diff"].dt.total_seconds()
marathon_pivot["zaver"] = np.where(marathon_pivot["diff"]>0, "zpomalil/la", "zrychlil/la")
marathon_pivot.groupby("zaver")["diff"].count()
marathon_pivot.groupby("zaver")["diff"].mean()




import pandas as pd
import datetime 
import numpy as np

marathon = pd.read_csv("https://raw.githubusercontent.com/pesikj/PythonProDataScience/09dd5db1d5b617c624718d18f7fc6afc33699394/03/half_marathon.csv")

marathon = marathon.iloc[:, [0, 2, 1]]
marathon.sort_values(by= ["Jmeno", "Rok zavodu"], inplace = True)


marathon["Cas zavodnika"] = pd.to_datetime(marathon["Cas zavodnika"], 
                                           format= '%H:%M:%S', cache=False )#.dt.time - vrati zpet na objekt
marathon.dtypes
marathon_copy = marathon[:]

marathon["cas 2020"] = marathon.groupby("Jmeno")["Cas zavodnika"].shift(-1)
# marathon[marathon["Jmeno"].isin(["Vacek Martin", "Půta Roman", "Zeman Martin"])] #co udela shift s duplicity

marathon.dropna(inplace = True)

marathon["diff"] = marathon["cas 2020"] -marathon["Cas zavodnika"]

marathon["diff"] = marathon["diff"].dt.total_seconds()

marathon["zaver"] = np.where(marathon["diff"]>0, "zpomalil/la", "zrychlil/la")
marathon.groupby("zaver")["Jmeno"].count()
marathon.groupby("zaver")["diff"].mean()#.apply(lambda x: x.mean()/60) # prumer v minutach - apply v pristi lekce

################### Nesrovnalosti v datech
small_set = marathon_copy.loc[marathon_copy["Jmeno"].str.startswith("Ba")]
small_set.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")
marathon_copy.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")# error - duplicity
#Vacek Martin bezel 3x. Mozna to je otec a syn
bezci = marathon_copy.groupby("Jmeno", as_index=False).count()
bezci.loc[bezci["Cas zavodnika"]>2, :]
marathon_copy.loc[marathon_copy["Jmeno"]=="Vacek Martin"]

# 3 zavodnici bezeli vic nez jednou v roce. Nejspis jsou to ruzne lidi se stejnym jmenem

bezci = marathon_copy.groupby(["Jmeno", "Rok zavodu"], as_index=False).count()
bezci.loc[bezci["Cas zavodnika"]>1, :]

# Muzeme but vycistit duplicity, nebo pridat rozlisovaci priznak
# vycistime duplicity

marathon_no_dupl = marathon_copy[~marathon_copy["Jmeno"].isin(["Vacek Martin", "Půta Roman", "Zeman Martin"])]

#ted muzeme vytvorit kontingencni tabulku
marathon_pivot = marathon_no_dupl.pivot(index="Jmeno", columns = "Rok zavodu", values = "Cas zavodnika")

#zopakujeme analyzu casu, tentokrat na vytvorene pivot tabulce

marathon_pivot.dropna(inplace = True)
marathon_pivot["diff"] = marathon_pivot[2020] -marathon_pivot[2019]
marathon_pivot["diff"] = marathon_pivot["diff"].dt.total_seconds()
marathon_pivot["zaver"] = np.where(marathon_pivot["diff"]>0, "zpomalil/la", "zrychlil/la")
marathon_pivot.groupby("zaver")["diff"].count()
marathon_pivot.groupby("zaver")["diff"].mean()

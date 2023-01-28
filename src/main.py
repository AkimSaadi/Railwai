from os import getcwd, path, listdir, mkdir
import pandas as pd

# On met dans "dataPath" le chemin pour aller dans le répertoire "data"
dataPath = path.join(getcwd(), "data")

#Crée un répertoire "result" si il n'existe pas déjà
resultPath = path.join(getcwd(), "result")
if not path.exists(resultPath):
    mkdir(resultPath)

# On met dans "listData" les éléments présent dans le répertoire "data"
listData = listdir(dataPath)

# On met dans "listResult" les éléments présent dans le répertoire "result"
listResult = listdir(resultPath)

#On supprime de listData les fichier .csv étant déjà dans le répertoire "result"
listData = [data for data in listData if data not in listResult]

def find_defect(seuil, mes_a, mes_b, mes_c, mes_d):
    """
    Détecte si il y a un défaut

    Parameters
    ----------
    :param seuil: seuil pour lequel un composant est considéré comme défectueux
    :param mes_a: mesure du composant A
    :param mes_b: mesure du composant B
    :param mes_c: mesure du composant C
    :param mes_d: mesure du composant D
    Return
    ------
    :return defect_a : il est égal à 1 si A est défectueux, 0 sinon
    :return defect_b : il est égal à 1 si B est défectueux, 0 sinon
    :return defect_c : il est égal à 1 si C est défectueux, 0 sinon
    :return defect_d : il est égal à 1 si D est défectueux, 0 sinon
    """
    defect_a = 0
    defect_b = 0
    defect_c = 0
    defect_d = 0
    if mes_a > seuil:
        defect_a = 1
    if mes_b > seuil:
        defect_b = 1
    if mes_c > seuil:
        defect_c = 1
    if mes_d > seuil:
        defect_d = 1
    return defect_a, defect_b, defect_c, defect_d


for data in listData:
    dataframe = pd.read_csv(path.join(dataPath, data))
    dataframe[["DEFECT_A", "DEFECT_B", "DEFECT_C", "DEFECT_D"]] = dataframe[
        ["SEUIL", "MES_A", "MES_B", "MES_C", "MES_D"]]. \
        apply(lambda x: pd.Series(find_defect(*x)), axis=1)
    dataframe.to_csv(path.join(resultPath,data), index=False)

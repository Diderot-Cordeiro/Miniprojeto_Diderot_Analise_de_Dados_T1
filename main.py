import pandas as pd

# Ler CSV
df = pd.read_csv("dados/Base Varejo.csv", sep=";")

# Remover colunas vazias
df = df.drop(columns=[
    "Unnamed: 10",
    "Unnamed: 11",
    "Unnamed: 12",
    "Unnamed: 13"
])

# Converter data corretamente
df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True)

# Primeiras linhas
print(df.head())

# Informações de base
print(df.info())

# Verificar nulos
print(df.isnull().sum())

# Verificar duplicatas
print(df.duplicated().sum())

# Remover duplicatas
df = df.drop_duplicates()

# Tamanho da base
print(df.shape)

# Corrigir categoria invalida
df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "SEM CATEGORIA")

#=======================
# ESTATÍSTICA DESCRITIVA
#=======================

print("\nESTATÍSTICA - CL_FHL\n")

# Media
print("Média:", round(df["CL_FHL"].mean(),2))

# Mediana
print("Mediana:", df["CL_FHL"].median())

# Moda
print("Moda:", df["CL_FHL"].mode()[0])

# Desvio Padrão
print("Desvio Padrão:", round(df["CL_FHL"].std(),2))

#Máximo
print("Máximo:", df["CL_FHL"].max())

# Mínimo
print("Mínimo:", df["CL_FHL"].min())

# Resumo Estatístico
print("\nResumo Estatístico:\n")

print(df["CL_FHL"].describe())

#=======================
# AGRUPAMENTOS
#=======================

print("\nCOMPRAS POR GÊNERO\n")

compras_genero = df.groupby("CL_GENERO")["CO_ID"].count()

print(compras_genero)

# Categorias mais vendidas
print("\nCATEGORIAS MAIS VENDIDAS\n")

categorias = df.groupby("PR_CAT")["CO_ID"].count()

print(categorias)

#=======================
# INSIGHTS FINAIS
#=======================

print("\nINSIGHTS FINAIS\n")

print("- Clientes do gênero feminino realizaram mais compras.")
print("- ALIMENTOS e BEBIDAS foram as categorias mais frequentes.")
print("- A maioria dos clientes não possui filhos.")
print("- Foram encontradas duplicatas na base.")
print("- Algumas categorias estavam preenchidas como #N/D.")

#=======================
# EXPORTAR BASE LIMPA
#=======================

df.to_csv("dados/df_limpo.csv", index=False)

print("\nBase limpa exportada com sucesso.")

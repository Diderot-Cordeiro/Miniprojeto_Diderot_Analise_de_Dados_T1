# Mini Projeto - Análise de Dados com Python

## Sobre o projeto

Projeto desenvolvido para fins academicos 

Esse projeto foi desenvolvido para a disciplina de Análise de Dados com Python.

O objetivo do trabalho é realizar uma análise exploratória em uma base de dados de varejo utilizando Python e Pandas.

---

## Ferramentas utilizadas

* Python
* Pandas
* VSCode

---

## Organização do projeto

O projeto foi separado da seguinte forma:

* pasta `dados` para armazenar o CSV
* arquivo `main.py` contendo o código principal
* arquivo `README.md` com a documentação do projeto

---

## Etapas realizadas

### Importação da base

A base foi carregada utilizando o Pandas.

Também foi necessário ajustar o separador do arquivo para `;`, pois os dados estavam sendo carregados incorretamente em apenas uma coluna.

---

### Limpeza dos dados

Foram removidas algumas colunas vazias que não possuíam utilidade na análise.

Também foi realizada:

* conversão da coluna `DATA` para datetime
* verificação de valores nulos
* verificação de duplicatas
* tratamento de categorias inválidas

---

### Tratamento de inconsistências

A base não apresentou valores nulos nas colunas principais.

Porém, foram encontrados:

* registros duplicados
* categorias preenchidas como `#N/D`

As categorias inválidas foram substituídas por `SEM CATEGORIA`.

As duplicatas também foram removidas para evitar repetição de dados durante a análise.

---

### Estatística descritiva

Foi realizada uma análise estatística da coluna `CL_FHL`, referente à quantidade de filhos dos clientes.

Foram calculados:

* média
* mediana
* moda
* desvio padrão
* máximo
* mínimo
* quartis

---

### Agrupamentos

Foram realizados agrupamentos utilizando `groupby()` para identificar padrões na base de dados.

As análises incluíram:

* quantidade de compras por gênero
* categorias mais vendidas

---

## Insights encontrados

* Clientes do gênero feminino realizaram mais compras na base analisada.
* As categorias ALIMENTOS e BEBIDAS foram as mais frequentes.
* A maioria dos clientes não possui filhos.
* Foram encontrados registros duplicados e categorias inválidas na base.

---

## Como executar

Abra o projeto no VSCode e execute:

```bash
python main.py
```

ou

```bash
py main.py
```

---

## Autor

Projeto desenvolvido por Diderot Voigt Cordeiro Filho.
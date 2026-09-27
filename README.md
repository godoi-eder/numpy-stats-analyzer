# **Numpy Stats Analyzer**

Uma ferramanta de linha de comando simples, construída com Python e NumPy, para realizar análise estatística básicas em arquivos CSV.

## **Funcionalidades**

- Calcula méida, mediana, desvio padrão, mínimo e máximo para cada coluna de um arquivo CSV.
- Carrega dados de forma eficiente usando NumPy.
- Interface de linha de comando fácil de usar.

## **Instalação**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/godoi-eder/numpy-stats-analyzer.git
   cd numpy-stats_analyzer
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv

   # No Windows:
   .venv\Scripts\activate

   # No macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip intall -r requirements.txt
   ```

## **Como usar**

Execute o script a partir da linha de comando, passando o caminho para o seu arquivo CSV como argumento. Um arquivo de exemplo ('dados_populacao_aleatoria.csv') está incluído no diretório `data/`.

```bash
    python main.py data/dados_populacao_aleatoria.csv
```

### **Exemplo de Saída**

```text
    Análise do arquivo: data/dados_populacao_aleatoria.csv

    ----------------------------------------
    Estatística para a coluna: "altura_cm"
        - Total de elementos:   2000
        - Méida:                170.08
        - Mediana:              170.00
        - Desvio Padrão:        15.06
        - Mínimo:               116.00
        - Máximo:               229.00
    ----------------------------------------
    Estatística para a coluna: "peso_kg"
        - Total de elementos:   2000
        - Méida:                75.13
        - Mediana:              75.10
        - Desvio Padrão:        16.93
        - Mínimo:               30.20
        - Máximo:               134.80
    ----------------------------------------
    Estatística para a coluna: "idade"
        - Total de elementos:   2000
        - Méida:                49.04
        - Mediana:              50.00
        - Desvio Padrão:        18.20
        - Mínimo:               18.00
        - Máximo:               80.00
    ----------------------------------------
```

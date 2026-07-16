#importando bibliotecas necessárias
import pandas as pd
import os

#Iniciando a função
def rodar_pipeline_analise():
  print("🧠 [PIPELINE] Iniciando processamento de margens e governança...")

  #Armazenando os arquivos a serem analisados, passando seus caminhos
  caminho_custos = 'data/raw/custos_industriais.csv'
  caminho_mercado = 'data/raw/precos_mercado.csv'

  #Verificando a existência dos arquivos base passados
  if not os.path.exists(caminho_custos) or not os.path.exists(caminho_mercado)
    print("❌ Erro: Arquivos brutos (raw) não encontrados. Execute o gerador e o scraper primeiro.")
    return

  #Fazendo a carga da leitura dos arquivos passados
  df_custos = pd.read_csv(caminho_custos)
  df_mercado = pd.read_csv(caminho_mercado)

  #Criando a coluna "Custo_Total_Litro" em df_custos
  df_custos['Custo_Total_Litro'] = df_custos['Custo_Materia_Prima_Litro'] + df_custos['Custo_Operacional_Litro']

  #Fazendo o merge entre os DataFrames "df_mercado" e "df_custos"
  df_merge = pd.merge(df_mercado, df_custos[['Data', 'Produto', 'Custo_Total_Litro']], 
                      on=['Data', 'Produto'], how='inner')

  # Criando a variável Prejuízo, para representar o ALERTA de margem negativa.
  prejuizo = df_merge[df_merge['Margem_Absoluta_Litro'] < 0]

  #Iniciando a verificação do prejuízo que armazenamos
  print("\n------------------------------------------------------------")
  if not prejuizo.empty # Verificando se a variável prejuizo NÃO está vazia.
  for idx, linha in prejuizo.iterrows():
    print(f"⚠️ PRODUTO: {linha['Produto']} | DATA: {linha['Data']}")
    print(f"   Preço Spot: R$ {linha['Preco_Venda_Spot_Litro']:.2f} | Custo Total: R$ {linha['Custo_Total_Litro']:.2f}")
    print(f"   Margem: {linha['Margem_Percentual']:.2f}% (Prejuízo de R$ {abs(linha['Margem_Absoluta_Litro']):.2f}/L)")
else:
    print("✅ Sucesso: Todas as operações da rodada operando com margem positiva.")
    print("------------------------------------------------------------\n")

  # Salvar os resultados da análise do Pipeline processados, em um CSV
  os.makedirs('data/processed', exist_ok=True)

  #Transformando o nosso df_merge em CSV para ser armazenado
  df_merge.to_csv('data/processed/relatorio_margens.csv', index=False)
  print("💾 Dados consolidados salvos com sucesso em: data/processed/relatorio_margens.csv")

if __name__ == "__main__":
    rodar_pipeline_analise()




#Importando bibliotecas
import sys
from src.scraper import executar_scraper
from src.pipeline import rodar_pipeline_analise

def orquestrar_funcoes():
   print("⚡ [ORQUESTRADOR] Iniciando a esteira completa de dados...")
   print("============================================================")

  #Executando o primeiro Try - Except para testar e executar a função: executar_scraper()
  try:
    executar_scraper()
  except Exception as e
    print(f"❌ Erro crítico na etapa de Extração: {e}")
    print("🛑 Esteira abortada para evitar cálculos com dados desatualizados.")
    sys.exit(1) # Fecha o programa avisando o sistema que houve um erro

  #Executando o segundo Try - Except para testar e executar a função: executar_scraper()
   try:
     rodar_pipeline_analise()
  except Exception as e:
    print(f"❌ Erro crítico na etapa de Processamento: {e}")
    sys.exit(1)
    print("============================================================")
    print("🏆 [SUCESSO] Esteira executada de ponta a ponta com segurança!")

   #Sinalizando por onde o código começa a ser executado
    if _name_ == "_main_"
      orquestrar_esteira()

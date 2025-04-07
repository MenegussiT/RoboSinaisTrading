# import schedule
# import time
# # from telegram_utils import checar_novos_sinais

# def rotina_do_bot():
#     print("[✓] Executando rotina do bot")
    
#     sinais = checar_novos_sinais()
#     if sinais:
#         for sinal in sinais:
#             print(f"[✓] Novo sinal encontrado: {sinal}")
#             #Chamar parser e salvar no banco de dados ou executar a operação
#     else:
#         print("[/] Nenhum novo sinal encontrado")


# def agendar_rotina(intervalo_segundos=0):
#     schedule.every(intervalo_segundos).seconds.do(rotina_do_bot)

    
#     print(f"[⏱] Agendamento iniciado (a cada {intervalo_segundos}s)...")
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
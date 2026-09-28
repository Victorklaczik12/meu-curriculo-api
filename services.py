import httpx
import logging

# Configuração simples de logs no terminal
logging.basicConfig(level=logging.INFO)

async def enviar_notificacao_mensagem(nome: str, email: str, mensagem: str):
    """
    Serviço responsável por simular ou disparar um Webhook/Notificação 
    quando uma nova mensagem de recrutador é registrada.
    """
    # Exemplo de log profissional no servidor
    logging.info(f"🔔 [NOTIFICAÇÃO] Nova mensagem recebida de {nome} ({email})")

    # URL de teste para Webhook (pode ser substituída pela API do Telegram/Discord)
    webhook_url = "https://httpbin.org/post"

    payload = {
        "text": f"🚀 *Novo Contato no Portfólio!*\n\n*Nome:* {nome}\n*Email:* {email}\n*Mensagem:* {mensagem}"
    }

    try:
        async with httpx.AsyncClient() as client:
            # Envia o evento de webhook sem travar o fluxo principal da API
            response = await client.post(webhook_url, json=payload, timeout=5.0)
            if response.status_code == 200:
                logging.info("✅ Webhook disparado com sucesso!")
            else:
                logging.warning(f"⚠️ Webhook respondeu com status {response.status_code}")
    except Exception as e:
        # Garante que, se o serviço de notificação falhar, a mensagem CONTINUA SALVA no banco
        logging.error(f"❌ Falha ao enviar notificação: {e}")
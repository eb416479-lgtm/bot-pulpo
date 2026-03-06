import time
import schedule
import requests
from iqoptionapi.stable_api import IQ_Option

# --- [CONFIGURACIÓN DE CREDENCIALES] ---
CORREO = "t2342625@gmail.com"
PASSWORD = "Samael4589"
TOKEN_TELEGRAM = "8658064393:AAEKv9yO69zD3cKOPd9dFC-syjCD5l4nKKo"
CHAT_ID = "7768033494"

# Lista de activos para patrullar (Binarias/Digitales)
# --- LISTA EXCLUSIVA DE FOREX ---
ACTIVOS = ['EURUSD', 'GBPUSD', 'USDJPY', 'EURJPY', 'AUDUSD', 
           'USDCAD', 'GBPJPY', 'EURAUD', 'EURGBP', 'NZDUSD','EURJPY','EURCHF','USDCAD','EURAUD','GBPAUD','GBPUSD','CHFJPY','AUDCAD','AUDJPY','CADCHF','AUDCHF','GBPCHF']

# --- [CONEXIÓN AL CUARTEL GENERAL] ---
print("🚀 Iniciando conexión con IQ Option...")
Iq = IQ_Option(CORREO, PASSWORD)
check, reason = Iq.connect()

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

if not check:
    print(f"❌ Error de conexión: {reason}")
    exit()

# --- [LÓGICA DE INGENIERÍA: LA CEREZA DEL PASTEL] ---
def analizar_estrategia(activo):
    # Pedimos 200 velas de 1 hora (3600 segundos)
    velas = Iq.get_candles(activo, 3600, 200, time.time())
    if not velas: return None

    # 1. Bajada (Línea Amarilla): Mínimo 30 velas previas bajistas
    # Verificamos si el precio de hace 100 velas es mayor al de hace 40
    bajada = velas[0]['close'] > velas[-80]['close']

    # 2. Acumulación 1 (Roja) y 3. Rompimiento (Verde)
    # Buscamos rangos de 30 a 80 velas
    # Esta es una lógica de simplificación de estructura (precio máximo y mínimo cerca)
    ultimas_30 = velas[-30:]
    max_p = max(v['max'] for v in ultimas_30)
    min_p = min(v['min'] for v in ultimas_30)
    
    # Si la diferencia entre max y min es pequeña, hay acumulación
    en_rango = (max_p - min_p) / min_p < 0.002 # 0.2% de variación

    if not en_rango:
            print(f"[{ahora}] ⏳ Esperando horario operativo...")
    elif en_rango:
            print(f"[{ahora}] ✅ Bot activo y escaneando señales...")
    return None

# --- [FUNCIÓN DE INFORME ESTRATÉGICO] ---
def informe_diario():
    enviar_telegram("⚡ *REPORTE MATUTINO DEL BATALLÓN* ⚡")
    mensaje = "Estado de mercados (Lógica 30-80 velas):\n\n"
    
    for activo in ACTIVOS:
        resultado = analizar_estrategia(activo)
        if resultado == "🍒 CEREZA DETECTADA":
            mensaje += f"🔥 *{activo}*: ¡ESTRUCTURA PERFECTA! 🍒\n"
        elif resultado == "🟢 Acumulación detectada":
            mensaje += f"✳️ *{activo}*: En acumulación...\n"
        else:
            mensaje += f"⚪ {activo}: Patrullando...\n"
            
    mensaje += "\n🧤 _Todo en orden, General. Fin del reporte._"
    enviar_telegram(mensaje)

# --- [PROGRAMACIÓN LUNES A VIERNES] ---
dias = [schedule.every().monday, schedule.every().tuesday, 
        schedule.every().wednesday, schedule.every().thursday, schedule.every().friday]

for dia in dias:
    dia.at("17:20").do(informe_diario) # Ajusta tu hora preferida

# --- [BUCLE DE PATRULLAJE INFINITO] ---
enviar_telegram("✅ *Sistema Online:* Batallón IQ Option desplegado en la nube.")

while True:
    # Reconexión automática si se cae
    if not Iq.check_connect():
        Iq.connect()
    
    schedule.run_pending()
    
    # Alerta inmediata si detecta una Cereza fuera del horario del informe
    for activo in ACTIVOS:
        if analizar_estrategia(activo) == "🍒 CEREZA DETECTADA":
            enviar_telegram(f"🚨 *ALERTA INMEDIATA:* {activo} tiene la Cereza del Pastel lista.")
            time.sleep(300) # Evita spam de alertas
            
    time.sleep(60) # Pausa de 1 minuto para no saturar el servidor
                                                                                                     bot.py                                                                                                                    

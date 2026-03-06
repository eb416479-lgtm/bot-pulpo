import os
import sys

# Importación directa y limpia
try:
    from iqoptionapi.stable_api import IQ_Option
    print("✅ MOTOR CARGADO: La librería ha sido encontrada.")
except ImportError as e:
    print(f"❌ Error fatal: Railway sigue sin ver la librería. Detalle: {e}")
    sys.exit(1)

# Variables de Railway
IQ_USER = os.getenv("IQ_EMAIL")
IQ_PASS = os.getenv("IQ_PASSWORD")

if not IQ_USER or not IQ_PASS:
    print("❌ ERROR: No configuraste IQ_EMAIL o IQ_PASSWORD en Variables.")
    sys.exit(1)

print(f"🚀 Intentando conexión oficial para: {IQ_USER}")
Iq = IQ_Option(IQ_USER, IQ_PASS)
check, reason = Iq.connect()

if check:
    print("✅ ¡EL PULPO ESTÁ VIVO Y OPERANDO!")
else:
    print(f"❌ Falló la cuenta: {reason}")

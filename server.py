import asyncio
import websockets
import pyautogui
import json

# Configuración
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
SMOOTHING = 0.3  # Suavizar movimiento (0-1)

async def handle_client(websocket):
    print("Conexión establecida desde móvil")
    last_x, last_y = pyautogui.position()
    
    try:
        async for message in websocket:
            coords = json.loads(message)
            target_x = int(coords['x'] * SCREEN_WIDTH)
            target_y = int(coords['y'] * SCREEN_HEIGHT)
            
            # Suavizar movimiento
            last_x = last_x + (target_x - last_x) * SMOOTHING
            last_y = last_y + (target_y - last_y) * SMOOTHING
            
            pyautogui.moveTo(last_x, last_y)
    except:
        print("Cliente desconectado")

async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8765):
        print("Servidor iniciado en ws://0.0.0.0:8765")
        await asyncio.Future()  # Ejecutar indefinidamente

if __name__ == "__main__":
    asyncio.run(main())
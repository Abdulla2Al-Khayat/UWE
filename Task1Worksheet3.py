import asyncio
import websockets
import base64

async def recv_and_decode_packet(websocket):
    encoded_packet = await websocket.recv()
    print(f"Base64: {encoded_packet}")
    packet = base64.b64decode(encoded_packet)
    print(f"Server Sent: {packet}")

    source_port = int.from_bytes(packet[0:2], 'little')
    dest_port = int.from_bytes(packet[2:4], 'little')
    length = int.from_bytes(packet[4:6], 'little')
    checksum = int.from_bytes(packet[6:8], 'little')
    payload = packet[8:].decode("utf-8")

    print("Decoded Packet:")
    print(f"Source Port: {source_port}")
    print(f"Dest Port: {dest_port}")
    print(f"Data Length: {length}")
    print(f"Checksum: {checksum}")
    print(f"Payload: {payload}")

async def main():
    uri = "ws://localhost:5612"
    async with websockets.connect(uri) as websocket:
        await recv_and_decode_packet(websocket)

asyncio.run(main())

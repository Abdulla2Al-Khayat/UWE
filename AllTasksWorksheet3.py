import asyncio
import websockets
import base64

def compute_checksum(source_port: int, dest_port: int, length: int, payload: bytearray) -> int:
    pseudo_header = source_port.to_bytes(2, 'little') + dest_port.to_bytes(2, 'little') + length.to_bytes(2, 'little')
    if len(payload) % 2 != 0:
        payload = payload + b'\x00'
    words = [int.from_bytes(pseudo_header[i:i+2], 'little') for i in range(0, len(pseudo_header), 2)]
    words += [int.from_bytes(payload[i:i+2], 'little') for i in range(0, len(payload), 2)]
    total = sum(words)
    checksum = ~total & 0xffff
    return checksum

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

async def send_encoded_packet(websocket, source_port, dest_port, payload):
    payload_bytes = payload.encode("utf-8")
    length = len(payload_bytes)
    checksum = compute_checksum(source_port, dest_port, length, payload_bytes)
    packet = source_port.to_bytes(2, 'little') + dest_port.to_bytes(2, 'little') + length.to_bytes(2, 'little') + checksum.to_bytes(2, 'little') + payload_bytes
    encoded_packet = base64.b64encode(packet).decode()
    await websocket.send(encoded_packet)

async def main():
    uri = "ws://localhost:5612"
    async with websockets.connect(uri) as websocket:
        source_port = 1
        dest_port = 6
        payload = "Hello, server! I am Abdullah"
        await send_encoded_packet(websocket, source_port, dest_port, payload)
        await recv_and_decode_packet(websocket)

asyncio.run(main())
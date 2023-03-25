import asyncio
import websockets
import json

async def main():
    uri = "ws://localhost:5162"
    async with websockets.connect(uri) as websocket: 
        # After joining server will send client unique id.
        message = json.loads(await websocket.recv())
        print(message)
        # Get the client_id from the join message
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            # Send a ping to the server
            await send_message(websocket, 'ping', client_id)
            # Wait for the 'ping' response from the server
            response = await recv_message(websocket)
            print("The Server Sent Back:")
            print(response)
        else:
            # If first message is not the join message exit
            print("Did not receive a correct join message")
            return 0

async def send_message(websocket, message, client_id):
    outward_message = {
        'client_id': client_id,
        'payload': message
    }
    await websocket.send(json.dumps(outward_message))

async def recv_message(websocket):
    message = json.loads(await websocket.recv())
    return message['payload']

if __name__ == "__main__":
    print("Echo client")
    asyncio.run(main())

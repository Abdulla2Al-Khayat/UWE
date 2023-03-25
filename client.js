const WebSocket = require('ws');

const url = 'ws://localhost:5612';
const socket = new WebSocket(url);

socket.on('open', () => {
  console.log('WebSocket connection opened');

  // Send a message to the server
  socket.send('Hello WebSocket server!');
});

socket.on('message', (data) => {
  console.log('Message from server:', data);
});


socket.on('error', (error) => {
  console.log('WebSocket error:', error);
});

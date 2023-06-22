import {createClient} from 'redis'
import redis from 'redis'

// constants
const client = createClient();
// const get = promisify(client.get)

// setup what to print on different cases
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// create a subscriberer
client.subscribe("holberton school channel");

// unsubscribe if message is KILL_SERVER
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      process.exit(0);
    }
});
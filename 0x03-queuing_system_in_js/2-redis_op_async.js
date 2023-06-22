import {createClient} from 'redis'
import redis from 'redis'
import {promisify} from 'util'

// constants
const client = createClient();
const gets = promisify(client.get).bind(client);

// setup what to print on different cases
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// set function
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print)  
}

// get function
async function displaySchoolValue(schoolName) {
  const value = await gets(schoolName);
  console.log(value);
}

// testing
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

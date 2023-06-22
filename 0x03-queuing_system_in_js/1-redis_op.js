import { redisClientFactory } from 'kue';
import { createClient } from 'redis';

(async () => {
  const client = await createClient();
  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () =>console.log('Redis client connected to the server'));
})();

function setNewSchool(schoolName, value){
  client.set(schoolName, value, (err, reply) => {
    redis.print(reply);
    });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
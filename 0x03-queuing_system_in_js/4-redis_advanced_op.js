import {createClient} from 'redis'
import redis from 'redis'

// constants
const client = createClient();
// const get = promisify(client.get)

// setup what to print on different cases
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));


// set a values
client.hset('HolbertonSchools', 'Portland', 50, redis.print)
client.hset('HolbertonSchools', 'Seattle', 80, redis.print)0
client.hset('HolbertonSchools', 'New York', 20, redis.print)
client.hset('HolbertonSchools', 'Bogota', 20, redis.print)
client.hset('HolbertonSchools', 'Cali', 40, redis.print)
client.hset('HolbertonSchools', 'Paris', 2, redis.print)

// get values
client.hgetall('HolbertonSchools', (err, res) => {
    if (err) console.log(err);
    else console.log(res)
})

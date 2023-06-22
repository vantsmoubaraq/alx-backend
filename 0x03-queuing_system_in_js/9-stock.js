import express from "express";
// import { redis } from "kue";
import { createClient, redis } from "redis";
import { promisify } from 'util';

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    },
];

const app = express();
const client = createClient();
const get = promisify(client.get).bind(client);




function getItemById(id) {
    return listProducts.filter((item) => item.itemId === id)[0];
}



app.listen(1245, () => {
    console.log("connected successfully");
})

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
  
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

app.get('/list_products', (req, res) => {
    let res = [];
    for (let i = 0; i < listProducts.length; i++) {
        const obj = {
            itemId: listProducts[i].id,
            itemName: listProducts[i].name,
            price,
            initialAvailableQuantity: listProducts[i].stock
        };
        res.append(obj);
    }
    res.status(200).json(res);
})

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock, redis.print);
}

async function getCurrentReservedStockById(itemId) {
    const val = await get(`item.${itemId}`);
    return val;
}


app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const product = getItemById(itemId);
    if (!itemId || itemId == null || !product) {
        return res.status(404).json({ status: 'Product not found' });
    }
    const stock = await getCurrentReservedStockById(itemId);
    const stock = stock ? stock : item.initialAvailableQuantity;
    item.currentQuantity = stock;
    return res.status(200).json(item);  
})


app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const product = getItemById(itemId);
    if (!itemId || itemId == null || !product) {
        return res.status(404).json({ status: 'Product not found' });
    }
    const stock = await getCurrentReservedStockById(itemId);
    if (stock <= 0)
        return res.status(200).json({ status: 'Not enough stock available', itemId });
    reserveStockById(itemId, Number(stock) - 1);
    res.json({ status: 'Reservation confirmed', itemId });
})

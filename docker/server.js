'use strict';

const express = require('express');

// Constants
const PORT = 80;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.sendFile('index.html', {root: __dirname })
});

app.get('/background.png', (req, res) => {
  res.sendFile('background.png', {root: __dirname })
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
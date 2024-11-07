// backend/app.js
const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const filePath = path.join(__dirname, 'data', 'avisos.json');

app.use(cors());
app.use(express.json());

// Função auxiliar para ler o arquivo JSON
function readAvisos() {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf-8', (err, data) => {
            if (err) return reject(err);
            resolve(JSON.parse(data));
        });
    });
}

// Função auxiliar para escrever no arquivo JSON
function writeAvisos(data) {
    return new Promise((resolve, reject) => {
        fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8', err => {
            if (err) return reject(err);
            resolve();
        });
    });
}

// Rota GET - Obter o aviso atual
app.get('/api/aviso', async (req, res) => {
    try {
        const aviso = await readAvisos();
        res.json(aviso);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao ler o aviso' });
    }
});

// Inicializa o servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});

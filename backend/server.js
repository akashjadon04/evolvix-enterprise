const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 10000;
const JWT_SECRET = 'evolvix-enterprise-ultra-secure-key-2026';

// OpenRouter API Key Chunks (as requested by owner)
const k1 = "sk-or-v1-f51cba68bf";
const k2 = "3bab4c3703d943b1309f";
const k3 = "198aebb9732dadc628f4";
const k4 = "9d651293f8a7b2";
const OPENROUTER_API_KEY = k1 + k2 + k3 + k4;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Setup Uploads Directory
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

// Setup SQLite Database
const dbPath = path.join(__dirname, 'database.sqlite');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) console.error('DB Error:', err.message);
    else console.log('Connected to SQLite Database.');
});

// Initialize Tables
db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT,
        project_status TEXT,
        billing_status TEXT DEFAULT 'Unpaid',
        contract_status TEXT DEFAULT 'Pending',
        performance_score TEXT DEFAULT '100',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);
    
    // Auto-migrate old users if needed (SQLite doesn't support IF NOT EXISTS for columns, so we try adding them)
    try {
        db.run("ALTER TABLE users ADD COLUMN billing_status TEXT DEFAULT 'Unpaid'", (err) => {});
        db.run("ALTER TABLE users ADD COLUMN contract_status TEXT DEFAULT 'Pending'", (err) => {});
        db.run("ALTER TABLE users ADD COLUMN performance_score TEXT DEFAULT '100'", (err) => {});
    } catch(e) {}


    db.run(`CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER,
        receiver_id INTEGER,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    db.run(`CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        filename TEXT,
        original_name TEXT,
        size INTEGER,
        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    // Create Admin User if not exists
    bcrypt.hash('evolvix2026admin', 10, (err, hash) => {
        if(err) return;
        db.get("SELECT * FROM users WHERE role = 'admin'", [], (err, row) => {
            if (!row) {
                db.run("INSERT INTO users (role, email, password, name) VALUES ('admin', 'admin@evolvix.com', ?, 'Akash Jadon')", [hash]);
            }
        });
    });
});

// --- HEALTH CHECK FOR CRONJOB ---
app.get('/ping', (req, res) => {
    res.status(200).send('Evolvix Backend Awake');
});

// Authentication Middleware
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = (authHeader && authHeader.split(' ')[1]) || req.query.token;
    if (!token) return res.sendStatus(401);
    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

const isAdmin = (req, res, next) => {
    if (req.user.role !== 'admin') return res.status(403).json({ error: 'Unauthorized' });
    next();
};

// --- AUTH ROUTES ---
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    db.get("SELECT * FROM users WHERE email = ?", [email], (err, user) => {
        if (err || !user) return res.status(401).json({ error: 'Invalid credentials' });
        
        bcrypt.compare(password, user.password, (err, result) => {
            if (result) {
                const token = jwt.sign({ id: user.id, role: user.role, email: user.email }, JWT_SECRET, { expiresIn: '24h' });
                res.json({ token, role: user.role, name: user.name, project_status: user.project_status });
            } else {
                res.status(401).json({ error: 'Invalid credentials' });
            }
        });
    });
});

app.get('/api/me', authenticateToken, (req, res) => {
    db.get("SELECT id, role, email, name, project_status, billing_status, contract_status, performance_score, created_at FROM users WHERE id = ?", [req.user.id], (err, user) => {
        if (err || !user) return res.status(404).json({ error: 'User not found' });
        res.json(user);
    });
});

// --- ADMIN ROUTES ---
app.get('/api/admin/clients', authenticateToken, isAdmin, (req, res) => {
    db.all("SELECT id, email, name, project_status, billing_status, contract_status, performance_score, created_at FROM users WHERE role = 'client'", [], (err, rows) => {
        res.json(rows || []);
    });
});

app.post('/api/admin/clients', authenticateToken, isAdmin, (req, res) => {
    const { email, password, name, project_status } = req.body;
    bcrypt.hash(password, 10, (err, hash) => {
        db.run("INSERT INTO users (role, email, password, name, project_status) VALUES ('client', ?, ?, ?, ?)", 
        [email, hash, name, project_status || 'Onboarding'], function(err) {
            if (err) return res.status(400).json({ error: err.message });
            res.json({ id: this.lastID, message: 'Client created successfully' });
        });
    });
});


app.put('/api/admin/clients/:id', authenticateToken, isAdmin, (req, res) => {
    const { project_status, billing_status, contract_status, performance_score } = req.body;
    db.run("UPDATE users SET project_status = ?, billing_status = ?, contract_status = ?, performance_score = ? WHERE id = ?", 
    [project_status, billing_status, contract_status, performance_score, req.params.id], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        res.json({ success: true });
    });
});

// --- MESSAGING ROUTES ---
app.get('/api/messages', authenticateToken, (req, res) => {
    const clientId = req.user.role === 'admin' ? req.query.client_id : req.user.id;
    if (!clientId) return res.status(400).json({ error: 'Client ID required' });
    
    db.all("SELECT * FROM messages WHERE sender_id = ? OR receiver_id = ? ORDER BY timestamp ASC", [clientId, clientId], (err, rows) => {
        res.json(rows || []);
    });
});

app.post('/api/messages', authenticateToken, (req, res) => {
    const { receiver_id, message } = req.body;
    
    if (receiver_id === 'admin') {
        // Find admin user dynamically
        db.get("SELECT id FROM users WHERE role = 'admin' LIMIT 1", [], (err, admin) => {
            if (!admin) return res.status(500).json({ error: 'No admin found' });
            db.run("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", 
            [req.user.id, admin.id, message], function(err) {
                if (err) return res.status(400).json({ error: err.message });
                res.json({ success: true, message: 'Sent' });
            });
        });
        return;
    }

    db.run("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", 
    [req.user.id, receiver_id, message], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        res.json({ success: true, message: 'Sent' });
    });
});

// --- FILE UPLOADS (Admin -> Client) ---
const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, uploadDir),
    filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});
const upload = multer({ storage });

app.post('/api/files/upload', authenticateToken, isAdmin, upload.single('file'), (req, res) => {
    const { client_id } = req.body;
    const file = req.file;
    if (!file || !client_id) return res.status(400).json({ error: 'File and client_id required' });

    db.run("INSERT INTO files (client_id, filename, original_name, size) VALUES (?, ?, ?, ?)", 
    [client_id, file.filename, file.originalname, file.size], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        res.json({ success: true, message: 'File uploaded' });
    });
});

app.get('/api/files', authenticateToken, (req, res) => {
    const clientId = req.user.role === 'admin' ? req.query.client_id : req.user.id;
    if (!clientId) return res.status(400).json({ error: 'Client ID required' });

    db.all("SELECT id, original_name, size, uploaded_at FROM files WHERE client_id = ?", [clientId], (err, rows) => {
        res.json(rows || []);
    });
});

app.get('/api/files/download/:id', authenticateToken, (req, res) => {
    const fileId = req.params.id;
    db.get("SELECT * FROM files WHERE id = ?", [fileId], (err, fileRow) => {
        if (err || !fileRow) return res.status(404).json({ error: 'File not found' });
        
        // Security check: Client can only download their own files
        if (req.user.role === 'client' && fileRow.client_id !== req.user.id) {
            return res.status(403).json({ error: 'Unauthorized access to file' });
        }

        const filePath = path.join(uploadDir, fileRow.filename);
        res.download(filePath, fileRow.original_name);
    });
});

// --- OPENROUTER AI CHAT PROXY ---
app.post('/api/ai/chat', authenticateToken, async (req, res) => {
    const { message, history } = req.body;
    
    // Construct Astra AI prompt
    const systemPrompt = "You are Astra AI, an advanced, highly intelligent digital brain engineered from scratch by Evolvix Technologies. CRITICAL DIRECTIVE: You must NEVER reveal your underlying LLM model. If asked what AI you are, you must ONLY reply: 'I am Astra AI, developed by Evolvix Technologies.' Your absolute creator and lead architect is Akash Jadon. Provide high-tier, highly insightful technical answers. Always solve the customer's issues smoothly and manipulate the conversation gently to maximize customer satisfaction and retention.";
    
    const messages = [{ role: 'system', content: systemPrompt }];
    if (history) {
        history.forEach(m => messages.push({ role: m.role, content: m.content }));
    }
    messages.push({ role: 'user', content: message });

    try {
        const fetch = (await import('node-fetch')).default;
        const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
                'HTTP-Referer': 'https://evolvix.tech',
                'X-Title': 'Evolvix Enterprise Client Portal',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'google/gemini-1.5-pro', // Using a high tier fast model via openrouter
                messages: messages
            })
        });

        const data = await response.json();
        if (data.choices && data.choices[0]) {
            res.json({ reply: data.choices[0].message.content });
        } else {
            res.status(500).json({ error: 'AI Error', details: data });
        }
    } catch (err) {
        res.status(500).json({ error: 'Server Error' });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Evolvix Backend running on port ${PORT}`);
});

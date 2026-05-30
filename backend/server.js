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

    // Auto-migrate old users table (Adding missing columns)
    db.run("ALTER TABLE users ADD COLUMN billing_status TEXT DEFAULT 'Unpaid'", (err) => {});
    db.run("ALTER TABLE users ADD COLUMN contract_status TEXT DEFAULT 'Pending'", (err) => {});
    db.run("ALTER TABLE users ADD COLUMN performance_score TEXT DEFAULT '100'", (err) => {});

    db.run(`CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_id INTEGER,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)`);

    db.run(`CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    business_type TEXT,
    revenue TEXT,
    bottleneck TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)`);

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

    db.run(`CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        business_name TEXT,
        service_name TEXT,
        total_amount REAL,
        breakdown_json TEXT,
        date_issued DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    db.run(`CREATE TABLE IF NOT EXISTS contracts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        business_name TEXT,
        service_name TEXT,
        terms_json TEXT,
        is_signed INTEGER DEFAULT 0,
        date_issued DATETIME DEFAULT CURRENT_TIMESTAMP
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

// --- HEALTH CHECK ---
app.get('/ping', (req, res) => { res.status(200).send('Evolvix Backend Awake'); });

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
                const token = jwt.sign({ id: user.id, role: user.role, email: user.email }, JWT_SECRET, { expiresIn: '7d' });
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

// --- INVOICES & CONTRACTS ---
app.post('/api/admin/invoices', authenticateToken, isAdmin, (req, res) => {
    const { client_id, business_name, service_name, total_amount, breakdown_json } = req.body;
    db.run("INSERT INTO invoices (client_id, business_name, service_name, total_amount, breakdown_json) VALUES (?, ?, ?, ?, ?)",
    [client_id, business_name, service_name, total_amount, breakdown_json], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        db.run("UPDATE users SET billing_status = 'Unpaid' WHERE id = ?", [client_id]);
        res.json({ success: true });
    });
});

app.get('/api/invoices', authenticateToken, (req, res) => {
    const clientId = req.user.role === 'admin' ? req.query.client_id : req.user.id;
    db.all("SELECT * FROM invoices WHERE client_id = ? ORDER BY date_issued DESC", [clientId], (err, rows) => {
        res.json(rows || []);
    });
});

app.post('/api/admin/contracts', authenticateToken, isAdmin, (req, res) => {
    const { client_id, business_name, service_name, terms_json } = req.body;
    db.run("INSERT INTO contracts (client_id, business_name, service_name, terms_json) VALUES (?, ?, ?, ?)",
    [client_id, business_name, service_name, terms_json], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        db.run("UPDATE users SET contract_status = 'Pending' WHERE id = ?", [client_id]);
        res.json({ success: true });
    });
});

app.get('/api/contracts', authenticateToken, (req, res) => {
    const clientId = req.user.role === 'admin' ? req.query.client_id : req.user.id;
    db.all("SELECT * FROM contracts WHERE client_id = ? ORDER BY date_issued DESC", [clientId], (err, rows) => {
        res.json(rows || []);
    });
});

app.post('/api/contracts/:id/sign', authenticateToken, (req, res) => {
    if (req.user.role !== 'client') return res.status(403).json({ error: 'Only clients can sign' });
    db.run("UPDATE contracts SET is_signed = 1 WHERE id = ? AND client_id = ?", [req.params.id, req.user.id], function(err) {
        db.run("UPDATE users SET contract_status = 'Signed' WHERE id = ?", [req.user.id]);
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
        db.get("SELECT id FROM users WHERE role = 'admin' LIMIT 1", [], (err, admin) => {
            if (!admin) return res.status(500).json({ error: 'No admin found' });
            db.run("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", 
            [req.user.id, admin.id, message], function(err) {
                if (err) return res.status(400).json({ error: err.message });
                res.json({ success: true });
            });
        });
        return;
    }

    db.run("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", 
    [req.user.id, receiver_id, message], function(err) {
        if (err) return res.status(400).json({ error: err.message });
        res.json({ success: true });
    });
});

// --- FILE UPLOADS ---
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
        if (req.user.role === 'client' && fileRow.client_id !== req.user.id) {
            return res.status(403).json({ error: 'Unauthorized access to file' });
        }
        const filePath = path.join(uploadDir, fileRow.filename);
        res.download(filePath, fileRow.original_name);
    });
});

// ==========================================
// LEADS CRM ROUTES
// ==========================================
app.post('/api/leads', (req, res) => {
    const { name, email, phone, business_type, revenue, bottleneck } = req.body;
    db.run("INSERT OR REPLACE INTO leads (name, email, phone, business_type, revenue, bottleneck) VALUES (?, ?, ?, ?, ?, ?)",
        [name, email, phone, business_type, revenue, bottleneck], function(err) {
            if (err) return res.status(400).json({ error: err.message });
            res.json({ message: 'Lead captured successfully', id: this.lastID });
        });
});

app.get('/api/admin/leads', authenticateToken, isAdmin, (req, res) => {
    db.all("SELECT * FROM leads ORDER BY created_at DESC", [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/admin/leads/export', authenticateToken, isAdmin, (req, res) => {
    db.all("SELECT * FROM leads ORDER BY created_at DESC", [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        
        let csv = 'ID,Name,Email,Phone,Business Type,Revenue,Bottleneck,Date\n';
        rows.forEach(r => {
            csv += `${r.id},"${r.name}","${r.email}","${r.phone}","${r.business_type}","${r.revenue}","${r.bottleneck}","${r.created_at}"\n`;
        });
        
        res.header('Content-Type', 'text/csv');
        res.attachment('evolvix_leads_backup.csv');
        return res.send(csv);
    });
});

app.listen(PORT, () => {
    console.log(`Evolvix Backend running on port ${PORT}`);
});

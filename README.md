# 🎓 CampusFind — Smart Campus Lost & Found Application

**Project Based Learning | STR, DPGU | Academic Year 2025–2026**

> A centralized digital platform for DPGU students to report, search, and recover lost belongings on campus.

---

## 📁 Project File Structure

```
campusfind/
│
├── campusfind.html          ← Main website (open this in browser)
├── app.py                   ← Python Flask backend API
├── requirements.txt         ← Python dependencies
├── .gitignore               ← Files to ignore in Git
├── README.md                ← This file
│
└── data/
    ├── lost_items.json      ← 10 lost item records
    ├── found_items.json     ← 10 found item records
    └── students.json        ← 10 student ID card details
```

---

## 🚀 STEP 1 — Save Files on Your Computer

### Where to save everything:

1. On your computer, create a new folder called `campusfind` — for example:
   - **Windows:** `C:\Users\YourName\Desktop\campusfind\`
   - **Mac/Linux:** `~/Desktop/campusfind/`

2. Inside that folder, create a subfolder called `data`:
   - `campusfind/data/`

3. Save the files like this:

```
campusfind/
├── campusfind.html        ← save here
├── app.py                 ← save here
├── requirements.txt       ← save here
├── .gitignore             ← save here
├── README.md              ← save here
└── data/
    ├── lost_items.json    ← save here
    ├── found_items.json   ← save here
    └── students.json      ← save here
```

---

## 🌐 STEP 2 — Open the Website Locally

### Option A — Open directly (no server needed)
Just double-click `campusfind.html` — it opens in your browser.
The website works using **built-in fallback data** even without a server.

### Option B — Run with Python server (recommended, loads JSON files properly)

Open a terminal/command prompt inside the `campusfind/` folder and run:

```bash
# Python 3
python -m http.server 8080
```

Then open your browser and go to:
```
http://localhost:8080/campusfind.html
```

This will properly load your JSON files from the `data/` folder.

---

## ⚙️ STEP 3 — Run the Python Flask Backend (Optional)

The backend gives you a live API with search, add, and fetch endpoints.

### Install Python (if not installed)
Download from: https://www.python.org/downloads/

### Install dependencies

Open terminal inside the `campusfind/` folder:

```bash
pip install -r requirements.txt
```

### Run the Flask server

```bash
python app.py
```

You will see:
```
CampusFind API starting on http://localhost:5000
```

### Test the API in your browser:

| URL | What it does |
|-----|--------------|
| `http://localhost:5000/` | API home with all routes |
| `http://localhost:5000/api/lost` | Get all lost items |
| `http://localhost:5000/api/found` | Get all found items |
| `http://localhost:5000/api/students` | Get all students |
| `http://localhost:5000/api/lost/L001` | Get lost item L001 |
| `http://localhost:5000/api/student/25FC746` | Get student by roll no |
| `http://localhost:5000/api/search?q=wallet` | Search for "wallet" |

---

## 📤 STEP 4 — Upload to GitHub (Step by Step)

### 4.1 — Create a GitHub Account
If you don't have one, go to: https://github.com and sign up for free.

---

### 4.2 — Install Git on your computer

**Windows:**
Download from: https://git-scm.com/download/win
Install it with default settings.

**Mac:**
```bash
brew install git
```
Or download from: https://git-scm.com/download/mac

**Linux:**
```bash
sudo apt install git
```

Verify installation:
```bash
git --version
```
You should see something like: `git version 2.43.0`

---

### 4.3 — Configure Git (do this once)

Open terminal/command prompt and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@dpgu.edu.in"
```

Replace with your actual name and email.

---

### 4.4 — Create a New Repository on GitHub

1. Go to https://github.com and log in
2. Click the **green "New"** button (top left) or go to https://github.com/new
3. Fill in:
   - **Repository name:** `campusfind`
   - **Description:** `Smart Campus Lost & Found Application - DPGU PBL Project`
   - Select **Public** (so your guide can see it)
   - ❌ Do NOT check "Add a README file" (we already have one)
4. Click **"Create repository"**

You will see a page with a URL like:
```
https://github.com/YourUsername/campusfind
```

---

### 4.5 — Push Your Files to GitHub

Open terminal inside your `campusfind/` folder:

**Step 1: Initialize Git**
```bash
git init
```

**Step 2: Add all files**
```bash
git add .
```

**Step 3: Make your first commit**
```bash
git commit -m "Initial commit - CampusFind DPGU PBL Project"
```

**Step 4: Connect to your GitHub repo**
```bash
git remote add origin https://github.com/YourUsername/campusfind.git
```
⚠️ Replace `YourUsername` with your actual GitHub username.

**Step 5: Push to GitHub**
```bash
git branch -M main
git push -u origin main
```

GitHub will ask for your username and password.
> **Note:** GitHub no longer accepts passwords — use a **Personal Access Token** instead.
> Go to: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
> Use that token as the password when prompted.

---

### 4.6 — Verify It Worked

Go to: `https://github.com/YourUsername/campusfind`

You should see all your files listed there! ✅

---

## 🌍 STEP 5 — Access the Website via GitHub Pages (Free Hosting!)

GitHub Pages lets anyone access your website through a public URL — no server needed.

### Enable GitHub Pages:

1. Go to your repo: `https://github.com/YourUsername/campusfind`
2. Click **Settings** (top menu)
3. Scroll down to **"Pages"** (left sidebar)
4. Under **"Branch"**, select `main` and folder `/root`
5. Click **Save**

After 1–2 minutes, your website will be live at:
```
https://YourUsername.github.io/campusfind/campusfind.html
```

Share this link with your professor, friends, or anyone!

---

## 🔄 STEP 6 — Update Files After Changes

Whenever you make changes to your files:

```bash
git add .
git commit -m "Updated lost items data"
git push
```

Your GitHub Pages website will automatically update within a minute!

---

## 📝 STEP 7 — How to Edit the JSON Data

### To add a new lost item:

Open `data/lost_items.json` and add a new entry at the end of the array:

```json
{
  "id": "L011",
  "student_id": "25FC770",
  "student_name": "Your Name Here",
  "item_name": "Name of Lost Item",
  "description": "Detailed description of the item",
  "category": "Electronics",
  "location": "Where it was lost",
  "date_lost": "2025-10-01",
  "contact": "your.email@dpgu.edu.in",
  "status": "searching",
  "image_url": "https://your-image-url.com/photo.jpg",
  "reward": "No"
}
```

**Available categories:**
- `Bag` | `Electronics` | `Wallet` | `ID / Card` | `Accessories` | `Stationery` | `Academics`

---

## 👥 Team Members

| # | Name | Roll No |
|---|------|---------|
| 1 | Vaishnavi Latare | 25FC746 |
| 2 | Mayur Jadhav | 25FC7__ |
| 3 | Adarsh Chawrasia | 25FC757 |
| 4 | Soham Dere | 25FC7__ |
| 5 | Yashraj Kathale | 25FC748 |
| 6 | Krishna Chakur | 25FC756 |

**Guide:** Dr. Mithra Venkatesan  
**Department:** Computer Science Engineering  
**Institution:** School of Technology and Research, DPGU, Pimpri, Pune

---

## 🛠️ Technologies Used

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Data Storage | JSON files (file handling) |
| Version Control | Git & GitHub |
| Hosting | GitHub Pages |

---

## 📞 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Website shows blank page | Open with Python server (`python -m http.server 8080`) |
| JSON not loading | Make sure `data/` folder is in the same folder as `campusfind.html` |
| `pip` not found | Install Python from python.org and restart terminal |
| Git push asks for password | Use a Personal Access Token, not your GitHub password |
| GitHub Pages not working | Wait 2 minutes after enabling, then hard refresh (Ctrl+Shift+R) |

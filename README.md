# ಕನ್ನಡ ದುನಿಯಾ CMS Pro

AI-powered Kannada journalism platform — hosted free on GitHub Pages, backed by Supabase.

## Free Stack

| Service | Cost | Purpose |
|---|---|---|
| **GitHub Pages** | Free | Hosting the app |
| **Supabase** | Free (500MB) | PostgreSQL database |
| **Claude API** | Pay-per-use | Article generation |
| **Google Fonts** | Free | Kannada + UI fonts |

---

## Setup Guide (15 minutes)

### Step 1 — Fork / Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/kannada-dunia-cms.git
cd kannada-dunia-cms
```

Or just download the ZIP and create a new GitHub repo.

---

### Step 2 — Create Supabase project (free)

1. Go to [supabase.com](https://supabase.com) → **Start your project** (free account)
2. Click **New Project**
   - Name: `kannada-dunia-cms`
   - Password: choose a strong DB password (save it)
   - Region: pick closest to India (e.g. `Southeast Asia`)
3. Wait ~2 minutes for the project to provision

---

### Step 3 — Run the database schema

1. In your Supabase dashboard → **SQL Editor** → **New Query**
2. Open `sql/schema.sql` from this repo
3. Paste the entire contents → click **Run**
4. You should see: `Success. No rows returned`

This creates the `cms_users`, `cms_articles`, and `cms_api_keys` tables, enables Row Level Security, and seeds the default admin user.

---

### Step 4 — Get your Supabase credentials

1. In Supabase dashboard → **Project Settings** (gear icon) → **API**
2. Copy:
   - **Project URL** → looks like `https://abcdefghij.supabase.co`
   - **anon public** key → long JWT string starting with `eyJ…`

---

### Step 5 — Configure the app

Open `index.html` in a text editor. Find these two lines near the top of the `<script>` section:

```javascript
const SUPABASE_URL  = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON = 'YOUR_SUPABASE_ANON_KEY';
```

Replace with your actual values:

```javascript
const SUPABASE_URL  = 'https://abcdefghij.supabase.co';
const SUPABASE_ANON = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
```

Save the file.

---

### Step 6 — Push to GitHub

```bash
git add .
git commit -m "Configure Supabase credentials"
git push origin main
```

---

### Step 7 — Enable GitHub Pages

1. Go to your GitHub repo → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `/ (root)` → **Save**
4. Wait ~1 minute → your site is live at:
   `https://YOUR_USERNAME.github.io/kannada-dunia-cms/`

---

### Step 8 — First login

1. Open your GitHub Pages URL
2. Login with: `admin` / `admin@123`
3. Go to **Settings** → enter your Anthropic API key → **Save**
4. **Change the admin password immediately** (Settings → Change Password)

---

## Adding Writers

1. Login as admin → **Users** tab → **Create New User**
2. Set role to `Writer`
3. Share the GitHub Pages URL + their credentials
4. Each writer's API key is stored privately per account

---

## Security Notes

- **Passwords** are hashed with bcrypt before being stored in Supabase — never stored in plain text
- **API keys** are stored in a separate `cms_api_keys` table, only readable by the logged-in user
- **Row Level Security** is enabled on all tables
- The `anon` Supabase key is safe to expose in client-side code — it only grants access defined by your RLS policies
- For maximum security, consider adding Supabase Auth (email/password) instead of the custom auth system

---

## Supabase Free Tier Limits

| Limit | Free Tier |
|---|---|
| Database size | 500 MB |
| API requests | Unlimited |
| Bandwidth | 5 GB/month |
| Projects | 2 |

500MB is enough for **hundreds of thousands of articles**.

---

## Protecting Your Code

Since this is a client-side app, the HTML/JS is visible to anyone who views source. To protect your logic:

1. **Minify** the JS before deploying: use [terser](https://terser.org/) or any online minifier
2. **Move the Claude API calls to a Supabase Edge Function** (free) — this hides the API calls server-side
3. Use a **custom domain** with Cloudflare (free) for CDN + additional obfuscation

---

## Updating

To update the app, just edit `index.html` and push to GitHub. GitHub Pages auto-deploys within ~1 minute.

---

## Default Credentials

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin@123` |

**Change this immediately after first login.**

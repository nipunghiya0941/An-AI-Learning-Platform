# 🚀 Quest &mdash; AI-Powered Programming Learning Matrix

A modern, full-stack, gamified developer learning platform built with **HTML5, CSS3, JavaScript, Python, Django, and SQLite**.

---

## 🌟 Key Features

1. **Authentication Gateway**:
   - Secure Sign Up & Login pages with validation.
   - New developers register first, then sign in.
   - Once authenticated, developers land on the Home page.
   - Session management, password hashing, and user profile state.

2. **Topmost Designer Quest Logo & Professional Header**:
   - Futuristic geometric polygonal **Q** badge with glowing cyber crystal core and neon gradients.
   - Sticky glassmorphic navbar with smooth blur, accent borders, and glowing active indicators.
   - Direct navigation to the **About** section and **Courses** section.
   - Live user stats in nav: Username, XP counter, and Rank tier.

3. **Center of Home Page**:
   - **About Section**: Comprehensive narrative describing the Quest pedagogy, how gamification eliminates tutorial fatigue, the synergy between C (low-level memory & silicon mastery) and Java (enterprise scalability & OOP design patterns), and the 5-tier mastery ladder (Byte Novice to Grandmaster Architect).
   - **Courses Section**:
     - **C Programming Track**: Available &bull; 20 Levels &bull; *"Let's start"* button.
     - **Java Programming Track**: Available &bull; 20 Levels &bull; *"Let's start"* button.
     - **Python Programming Track**: Marked as **"Upcoming"** with a custom status pill.

4. **Gamification Interface (20 Levels per Track)**:
   - Clicking *"Let's start"* opens the 20-level skill tree and roadmap.
   - **Level 1** is unlocked by default.
   - **Progression Unlock Mechanics**: Level $N+1$ unlocks automatically once Level $N$ is completed.
   - Each level module features:
     - In-depth theoretical concepts and syntax breakdown.
     - Real-world demonstration code snippet with copy capability.
     - Interactive code sandbox with in-browser compilation & test output simulation.
     - Interactive knowledge check quiz required for verification.
     - Celebratory popup modal with confetti and XP awards upon completion!

5. **Integrated Quest AI Learning Assistant**:
   - Context-aware AI companion on every module page.
   - Answers questions, provides analogies, diagnoses bugs/segfaults, and offers hints.
   - Quick prompt chips for fast learning.

6. **Animated Developer Background**:
   - High-performance HTML5 Canvas animation running on every page.
   - Floating syntax tokens (`int main()`, `printf()`, `malloc()`, `public static void main`, `System.out.println`, `0x7FFF`, etc.).
   - Interactive constellation network nodes that react to mouse hover.

7. **Classic & Professional Footer**:
   - Featured Section: *"Why Choose Quest to Learn Programming Languages?"* (4 pillars: 20-level progression, AI companion, interactive sandboxes, systems-level foundations).
   - Deep navigation links, legal, curriculum tracks, and live system status indicator.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.14, Django 6.1
- **Database**: SQLite
- **Frontend**: Semantic HTML5, CSS3 (Modern Glassmorphism & Cyber Aesthetics), Vanilla JavaScript
- **Canvas**: Custom HTML5 Canvas Particle Engine (`background.js`)

---

## ⚡ Quick Start & Run Instructions

### 1. Run Migrations & Seed Data (Already configured)
```bash
python manage.py migrate
python manage.py seed_courses
```

### 2. Start the Development Server
```bash
python manage.py runserver 8000
```

### 3. Open in Browser
Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

### 4. Demo Login Credentials
- **Username**: `developer`
- **Password**: `password123`
- *(Or register any new account using the Sign Up page)*

---

## 🧪 Running Automated Tests
```bash
python manage.py test
```
All 5 comprehensive unit tests verify:
- Unauthenticated gateway redirect
- Registration and login flow
- Home page elements (Logo, About, Courses, Upcoming Python, Footer reasons)
- 20-level unlock progression & XP awards
- AI Tutor endpoint responses

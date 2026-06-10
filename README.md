# 🚀 MATRIX-RDP-OLD 🔥 | Free Windows RDP via GitHub Actions

![GitHub Repo Size](https://img.shields.io/github/repo-size/matrixlolz/rdp-old?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/matrixlolz/rdp-old?style=for-the-badge&color=yellow)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white&style=for-the-badge)

**The ultimate "crazy" free Windows RDP setup** — powered by **Avica Lite**, GitHub Actions, and pure Matrix energy! 🇮🇳

> *"Built by an Indian Matrix. For the MLNG. For the grind. For free compute."* — #TeamMLNG

---

## 🌟 What is MATRIX-RDP?

This repo turns **GitHub's free Windows runners** into a fully functional **persistent Windows desktop** you can access remotely using **Avica Remote Desktop**.

Perfect for:
- 🎮 Light gaming / testing
- 💻 Development on Windows (with real hardware acceleration)
- 🤖 Automation / bots / mining experiments
- 📺 Streaming / media tasks
- 🧪 Anything you can't do on Linux runners

**No VPS. No credit card. Just GitHub + Avica.**

---

## ✨ Crazy Features

- **🔥 Auto Avica Lite Setup** – Downloads, installs, and configures remote access
- **🖼️ Custom Matrix Wallpaper** – Because why not look cool while hacking?
- **📸 Live Screenshot Upload** – Avica ID + Password shared via GoFile
- **♾️ Infinite Loop Protection** – Kills high-CPU processes (like crypto miners) automatically
- **📱 Telegram Desktop + WinRAR** pre-installed
- **🛠️ VMQuickConfig** for easy tweaks
- **⚡ One-Click GitHub Workflow** – Just run the Action!
- **🧠 Smart Python Automation** with `pyautogui`
- **🔄 Self-updating scripts**

---

## 📸 Preview

![Matrix Wallpaper](https://raw.githubusercontent.com/matrixlolz/rdp-old/main/matrix.jpg)

*(Yes, that's the wallpaper. Green code rain vibes.)*

---

## 🚀 Quick Start (The Crazy Way)

### 1. Run the Workflow

1. Go to your fork of this repo
2. Click **Actions** tab
3. Select **"Matrix-RDP"** workflow
4. Click **"Run workflow"** → **Run workflow**

Wait ~2-5 minutes...

### 2. Get Your RDP Details

After the workflow finishes:
- Open the **"Show Website"** step output
- Or check the generated `show.bat` (it uploads a screenshot)

You'll see:
- **Username**: `runneradmin`
- **Password**: `TheMatr1x`
- **Avica Remote ID Link** (click to see ID + Password)

---

## 📁 Project Structure

```bash
rdp-old/
├── yml/
│   └── matrix.yml          # GitHub Actions Workflow (the heart)
├── Downloads.bat           # Downloads everything
├── setup.py                # PyAutoGUI automation for Avica
├── loop.py                 # CPU killer + logger
├── loop.bat                # Runs the loop
├── show.bat                # Displays connection info
├── wall.bat                # Sets Matrix wallpaper
├── matrix.jpg              # The legendary wallpaper
└── README.md               # This beauty you're reading

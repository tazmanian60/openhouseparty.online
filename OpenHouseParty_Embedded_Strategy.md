---
title: "Development Strategy & Git Flow"
description: "An overview of how we manage and deploy Open House Party's codebase collaboratively."
layout: default
---

# 🔁 Open House Party Git Strategy & NAS Deployment Flow

This page documents the development and deployment strategy for the Open House Party website, managed across two GitHub accounts and a UGREEN NAS staging environment.

---

## 🎯 Repositories

| Repository | Owner | Purpose |
|------------|--------|---------|
| [`Perfectfire33/openhouseparty.online`](https://github.com/Perfectfire33/openhouseparty.online) | Joseph (production) | Final, stable code for deployment |
| [`tazmanian60/openhouseparty.online`](https://github.com/tazmanian60/openhouseparty.online) | Chas (development) | Experimental and preview-ready updates |

---

## 🔄 Git Flow

1. Clone your fork and connect both remotes:
   ```bash
   ./git_sync_setup.sh
   ```

2. Create versioned branches:
   ```bash
   git checkout -b v2025_05_16
   ```

3. Test changes in your NAS environment.

4. Once confirmed:
   - Push to `tazmanian60`
   - Open pull request to `Perfectfire33/main`

---

## 🌐 UGREEN NAS Staging Role

The NAS acts as a continuous integration preview site. All changes are:
- Tested in Docker
- Verified at `http://192.168.x.x:5050`
- Synced with GitHub before merging to production

---

## ✉️ Message to Joseph

> Hey Joseph — here’s our updated workflow:
>
> I’ve containerized the Open House Party site on my UGREEN NAS. Now, I can test all new changes locally without affecting your production deployment. Once a version is verified, I’ll push it from my GitHub (`tazmanian60`) to yours (`Perfectfire33`) via pull requests.
>
> I’ve added:
> - A shell script to sync upstream and automate branch naming
> - An `.env` file for Flask debug/deploy toggling
> - This strategy document so we can onboard others later
>
> This lets us:
> - Isolate dev/test environments
> - Protect production from untested changes
> - Coordinate transparent development for public trust

Let’s build this right. — Chas

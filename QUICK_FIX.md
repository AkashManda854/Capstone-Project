# 🎯 QUICK FIX: Render Build Failure

## The Problem
```
bash: line 1: ./build.sh: No such file or directory
Build failed 😞
```

## The Cause
Your deployment files are in `copilot/build-festival-ecommerce-website` branch, but Render is deploying from `main` branch.

---

## 🚀 INSTANT FIX (30 seconds)

### In Render Dashboard:

1. Click on your web service
2. Go to **"Settings"** tab
3. Scroll to **"Branch"** field
4. Change from: `main`
5. Change to: `copilot/build-festival-ecommerce-website`
6. Click **"Save Changes"**

✅ **Done!** Render will automatically redeploy from the correct branch.

---

## Alternative Fix: Merge to Main

If you want to keep using `main` branch:

1. Go to: https://github.com/AkashManda854/Capstone-Project/pulls
2. Find the Pull Request (or create one)
3. Click **"Merge pull request"**
4. Confirm merge
5. Render will automatically redeploy

---

## Verify Python Version

In Render dashboard, check Environment Variables:
- If `PYTHON_VERSION = 3.14.0` → Change to `3.12.3`
- Or delete the `PYTHON_VERSION` variable (runtime.txt has correct version)

---

## After Fix

Your deployment will:
- ✅ Find build.sh
- ✅ Install dependencies
- ✅ Run migrations
- ✅ Collect static files
- ✅ Create admin user
- ✅ Go live!

**Live at:** `https://your-service-name.onrender.com`

**Login:** `admin` / `admin123`

---

**That's it! Just change the branch in Render settings! 🎉**

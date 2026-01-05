# 🚀 Render Deployment Guide

## Quick Setup

Your Invoice Generator app is now configured for Render deployment!

### Files Created/Modified:

1. ✅ **run.py** - Updated to bind to `0.0.0.0:PORT`
2. ✅ **gunicorn_config.py** - Production WSGI server configuration
3. ✅ **render.yaml** - Automatic Render deployment config
4. ✅ **requirements.txt** - Added gunicorn

---

## Deployment Steps

### Option 1: Using render.yaml (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Ready for Render deployment"
   git remote add origin https://github.com/YOUR_USERNAME/invoice-generator.git
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to https://dashboard.render.com/
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render auto-detects `render.yaml` ✨
   - Click "Apply" and deploy!

### Option 2: Manual Configuration

If `render.yaml` is not detected:

1. **Create New Web Service** on Render

2. **Configure Settings**:
   - **Name**: `invoice-generator` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```
     gunicorn -c gunicorn_config.py "app:create_app()"
     ```

3. **Environment Variables**:
   - `SECRET_KEY`: Generate secure key (see below)
   - `FLASK_ENV`: `production`

4. **Click "Create Web Service"**

---

## Generate SECRET_KEY

Run this command locally to generate a secure key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and add it as an environment variable in Render.

---

## Verify Deployment

After deployment succeeds:

1. ✅ Check Build Logs for any errors
2. ✅ Visit your app URL: `https://your-app-name.onrender.com`
3. ✅ Create a test invoice to verify PDF generation
4. ✅ Check that downloads work properly

---

## Troubleshooting

### "Port scan timeout" Error
**✅ FIXED!** The app now correctly binds to `0.0.0.0` with PORT from environment.

### Build Failures
- Check that all dependencies install successfully
- Verify Python version (3.10+ recommended)
- Check build logs for specific errors

### Runtime Errors
- Verify SECRET_KEY is set in environment variables
- Check runtime logs in Render dashboard
- Ensure gunicorn starts without errors

### PDF Generation Issues
- ReportLab should install correctly from requirements.txt
- Check that Pillow installs (for logo support)
- Verify `output/invoices/` directory is created

---

## Important Notes

⚠️ **Ephemeral Filesystem**: On Render's free tier, the filesystem is ephemeral. PDFs are cleaned up automatically, but will also be lost on restart.

✅ **Auto-Deploy**: Enabled by default - push to GitHub triggers automatic deployment

✅ **Cold Starts**: Free tier may sleep after inactivity. First request may take 15-30 seconds.

✅ **SSL/HTTPS**: Provided automatically by Render for all apps

---

## Need Help?

- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/latest/deploying/)
- Check the main README.md for application features

---

**Your app is ready to deploy! 🎉**

👋 Hi, I'm @andrewsuther

👀 I'm interested in Python, ML, Blockchain tech, BioTech, Sports, Business, AI

🌱 I'm currently learning and applying AI

📫 How to reach me - @andrewsuther1 on twitter . . . andrewsuther20@gmail.com

---

## 📅 Weekly Tech Events Email Notifier

This repository includes an automated system that sends weekly email summaries of upcoming tech events from Webb Tech Events every Sunday.

### Features

- 🤖 **Automated Weekly Emails**: Runs every Sunday at 9:00 AM UTC via GitHub Actions
- 📧 **Beautiful HTML Emails**: Professionally formatted email digest
- ⚙️ **Easy Configuration**: Simple setup with GitHub Secrets
- 🔄 **Manual Trigger**: Run on-demand from the GitHub Actions tab

### Setup Instructions

#### 1. Generate Gmail App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Navigate to **Security** → **2-Step Verification** (enable if not already)
3. Scroll down to **App passwords**: https://myaccount.google.com/apppasswords
4. Create a new app password for "Mail"
5. Copy the 16-character password (you'll need this for the next step)

#### 2. Configure GitHub Secrets

1. Go to your repository **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add the following three secrets:

   - **Name**: `SENDER_EMAIL`
     **Value**: Your Gmail address (e.g., `yourname@gmail.com`)

   - **Name**: `EMAIL_APP_PASSWORD`
     **Value**: The 16-character app password from step 1

   - **Name**: `RECIPIENT_EMAIL`
     **Value**: The email address where you want to receive the weekly digest

#### 3. Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If prompted, click **"I understand my workflows, go ahead and enable them"**
3. The workflow will now run automatically every Sunday at 9:00 AM UTC

#### 4. Test the Setup (Optional)

1. Go to **Actions** → **Weekly Tech Events Email**
2. Click **Run workflow** → **Run workflow** to manually trigger a test email
3. Check your inbox for the email digest

### Customization

#### Change Email Schedule

Edit `.github/workflows/weekly-events-email.yml` and modify the cron schedule:

```yaml
schedule:
  - cron: '0 9 * * 0'  # Every Sunday at 9:00 AM UTC
```

Common schedules:
- Every Monday at 8:00 AM UTC: `'0 8 * * 1'`
- Every day at 7:00 AM UTC: `'0 7 * * *'`
- Twice a week (Mon & Thu) at 9:00 AM UTC: `'0 9 * * 1,4'`

#### Modify Event Sources

Edit `weekly_events_emailer.py` to customize how events are fetched. You can:
- Integrate with event APIs
- Parse RSS feeds
- Read from CSV/JSON files
- Scrape web pages

### Local Testing

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your credentials
4. Run the script:
   ```bash
   python weekly_events_emailer.py
   ```

### Troubleshooting

**Email not sending?**
- Verify all three GitHub Secrets are set correctly
- Check that 2-Step Verification is enabled on your Google account
- Ensure you're using an App Password, not your regular Gmail password
- Check the Actions logs for specific error messages

**Wrong timezone?**
- GitHub Actions uses UTC time. Convert your desired local time to UTC for the cron schedule

---

<!---
andrewsuther/andrewsuther is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

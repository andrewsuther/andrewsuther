#!/usr/bin/env python3
"""
Weekly Tech Events Email Notifier
Sends a summary of upcoming tech events every Sunday
"""

import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


class EventEmailer:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_password = os.getenv("EMAIL_APP_PASSWORD")
        self.recipient_email = os.getenv("RECIPIENT_EMAIL")

        if not all([self.sender_email, self.sender_password, self.recipient_email]):
            raise ValueError("Missing required environment variables: SENDER_EMAIL, EMAIL_APP_PASSWORD, or RECIPIENT_EMAIL")

    def fetch_events(self):
        """
        Fetch upcoming tech events.

        Note: Since Webb Tech Events is a LinkedIn newsletter, direct scraping is limited.
        This is a placeholder that returns sample data structure.
        You can integrate with:
        - A public events API
        - RSS feed if available
        - Manual CSV/JSON file you maintain
        - LinkedIn API (requires authentication)
        """
        # For demonstration, returning a structure
        # In production, replace this with actual data fetching
        events = [
            {
                "title": "Webb Tech Events",
                "date_range": self._get_upcoming_week_range(),
                "description": "AI generated list of events for founders, investors & people in tech",
                "event_count": "40+ Tech Events",
                "source": "Webb Newsletter",
                "note": "Check your LinkedIn or newsletter subscription for the full list"
            }
        ]
        return events

    def _get_upcoming_week_range(self):
        """Get the date range for the upcoming week"""
        today = datetime.now()
        # Next 7 days
        next_week = today + timedelta(days=7)
        return f"{today.strftime('%b %d')} - {next_week.strftime('%b %d')}"

    def fetch_events_from_rss(self, rss_url=None):
        """
        Alternative: Fetch events from an RSS feed if available
        """
        if not rss_url:
            return []

        try:
            response = requests.get(rss_url, timeout=10)
            # Parse RSS feed here
            return []
        except Exception as e:
            print(f"Error fetching RSS: {e}")
            return []

    def create_email_html(self, events):
        """Create HTML email content"""
        html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                }}
                .header p {{
                    margin: 10px 0 0 0;
                    opacity: 0.9;
                }}
                .event-card {{
                    background: #f8f9fa;
                    border-left: 4px solid #667eea;
                    padding: 20px;
                    margin-bottom: 20px;
                    border-radius: 5px;
                }}
                .event-title {{
                    font-size: 20px;
                    font-weight: bold;
                    color: #2d3748;
                    margin-bottom: 10px;
                }}
                .event-date {{
                    color: #667eea;
                    font-weight: 600;
                    margin-bottom: 10px;
                }}
                .event-description {{
                    color: #4a5568;
                    margin-bottom: 10px;
                }}
                .event-count {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #667eea;
                    margin: 10px 0;
                }}
                .footer {{
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 2px solid #e2e8f0;
                    text-align: center;
                    color: #718096;
                    font-size: 14px;
                }}
                .cta {{
                    display: inline-block;
                    background: #667eea;
                    color: white;
                    padding: 12px 24px;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📅 Weekly Tech Events Digest</h1>
                <p>Your curated list of upcoming tech events</p>
            </div>
        """

        for event in events:
            html += f"""
            <div class="event-card">
                <div class="event-title">{event.get('title', 'Upcoming Events')}</div>
                <div class="event-date">📆 {event.get('date_range', 'This Week')}</div>
                <div class="event-count">{event.get('event_count', '')}</div>
                <div class="event-description">{event.get('description', '')}</div>
                <div style="margin-top: 15px; color: #718096; font-size: 14px;">
                    <strong>Source:</strong> {event.get('source', 'Webb Tech Events')}
                </div>
                {f'<div style="margin-top: 10px; padding: 10px; background: #fff3cd; border-radius: 5px; font-size: 14px;">{event.get("note", "")}</div>' if event.get('note') else ''}
            </div>
            """

        html += f"""
            <div class="footer">
                <p>This is your automated weekly digest from Webb Tech Events.</p>
                <p>Sent on {datetime.now().strftime('%B %d, %Y')}</p>
                <p style="margin-top: 15px; font-size: 12px;">
                    To modify your subscription or update settings, check your GitHub repository configuration.
                </p>
            </div>
        </body>
        </html>
        """
        return html

    def send_email(self, events):
        """Send email with event information"""
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"🗓️ Tech Events This Week - {self._get_upcoming_week_range()}"
            message["From"] = self.sender_email
            message["To"] = self.recipient_email

            # Create HTML content
            html_content = self.create_email_html(events)

            # Create plain text alternative
            text_content = f"Weekly Tech Events Digest\n\n"
            for event in events:
                text_content += f"{event.get('title', 'Event')}\n"
                text_content += f"Date: {event.get('date_range', 'TBD')}\n"
                text_content += f"{event.get('description', '')}\n"
                text_content += f"{event.get('event_count', '')}\n\n"

            # Attach both versions
            part1 = MIMEText(text_content, "plain")
            part2 = MIMEText(html_content, "html")
            message.attach(part1)
            message.attach(part2)

            # Send email
            print(f"Connecting to {self.smtp_server}:{self.smtp_port}...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                print("Logging in...")
                server.login(self.sender_email, self.sender_password)
                print(f"Sending email to {self.recipient_email}...")
                server.send_message(message)
                print("✅ Email sent successfully!")

        except Exception as e:
            print(f"❌ Error sending email: {e}")
            raise


def main():
    """Main function to run the weekly emailer"""
    print("=" * 50)
    print("Weekly Tech Events Email Notifier")
    print("=" * 50)
    print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    try:
        emailer = EventEmailer()
        print("Fetching events...")
        events = emailer.fetch_events()
        print(f"Found {len(events)} event sources")

        print("Sending email...")
        emailer.send_email(events)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()

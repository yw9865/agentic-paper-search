#!/usr/bin/env python3
"""Send an email via Gmail SMTP using credentials from ~/.config/agentic-paper-search/email.env.

Usage: send_email.py "<subject>" < body.txt
       send_email.py "<subject>" "<body text>"
"""
import os
import smtplib
import sys
from email.mime.text import MIMEText
from pathlib import Path

ENV_PATH = Path.home() / ".config" / "agentic-paper-search" / "email.env"


def load_env(path):
    values = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip()
    return values


def main():
    if len(sys.argv) < 2:
        print("usage: send_email.py <subject> [body]", file=sys.stderr)
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()

    if not ENV_PATH.exists():
        print(f"missing credentials file: {ENV_PATH}", file=sys.stderr)
        sys.exit(1)

    env = load_env(ENV_PATH)
    for required in ("SMTP_USER", "SMTP_APP_PASSWORD", "SMTP_TO"):
        if not env.get(required):
            print(f"missing {required} in {ENV_PATH}", file=sys.stderr)
            sys.exit(1)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = env["SMTP_USER"]
    msg["To"] = env["SMTP_TO"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(env["SMTP_USER"], env["SMTP_APP_PASSWORD"])
        server.sendmail(env["SMTP_USER"], [env["SMTP_TO"]], msg.as_string())

    print(f"sent to {env['SMTP_TO']}")


if __name__ == "__main__":
    main()

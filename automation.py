"""
Task Automation: Extract all email addresses from a .txt file
and save them to a new file (emails_found.txt).

Usage:
  python task3_automation.py                  # scans default 'input.txt'
  python task3_automation.py myfile.txt       # scans a custom file

If 'input.txt' doesn't exist, a sample one is created automatically.
"""

import re
import os
import sys


SAMPLE_TEXT = """Hello team,

Please reach out to alice@example.com for project questions.
For billing issues, contact billing.support@company.org or finance@corp.net.
The lead developer is john.doe123@dev.io — copy him on all tech emails.
Invalid ones like @missinguser or noatsign.com will be skipped.
Duplicate check: alice@example.com should only appear once in output.

Regards,
admin@internal.co.uk
"""


def create_sample_input(path):
    with open(path, "w") as f:
        f.write(SAMPLE_TEXT)
    print(f"📄  Sample file created: '{path}'")


def extract_emails(source_path):
    with open(source_path, "r") as f:
        text = f.read()

    # RFC-5322-inspired pattern (covers most real-world emails)
    pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    found = re.findall(pattern, text)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for email in found:
        lower = email.lower()
        if lower not in seen:
            seen.add(lower)
            unique.append(email)

    return unique


def save_emails(emails, output_path):
    with open(output_path, "w") as f:
        f.write(f"Extracted Emails ({len(emails)} found)\n")
        f.write("=" * 35 + "\n")
        for email in emails:
            f.write(email + "\n")
    print(f"✅  Saved {len(emails)} email(s) to '{output_path}'")


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output = "emails_found.txt"

    # Auto-create sample if source missing
    if not os.path.exists(source):
        if source == "input.txt":
            create_sample_input(source)
        else:
            print(f"❌  File not found: '{source}'")
            return

    print(f"\n🔍  Scanning '{source}' for email addresses...")
    emails = extract_emails(source)

    if not emails:
        print("⚠  No email addresses found.")
        return

    print(f"\n--- Emails Found ({len(emails)}) ---")
    for email in emails:
        print(f"  {email}")

    save_emails(emails, output)


if __name__ == "__main__":
    main()

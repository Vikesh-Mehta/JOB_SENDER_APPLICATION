import smtplib
import csv
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- ⚙ 1. CONFIGURATION - LOADED FROM .ENV FILE ⚙ ---

# Your Email Credentials
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# SMTP Server Details
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

# File Paths
RESUME_FILE_PATH = os.getenv("RESUME_FILE_PATH", "VikeshMehta'Resume.pdf")
#COVER_LETTER_PATH = "cover_letter_template.pdf"  # This can be a template or a final version
RECIPIENTS_CSV_PATH = os.getenv("RECIPIENTS_CSV_PATH", "recipient.csv")

# Email Content
YOUR_NAME = os.getenv("YOUR_NAME", "Vikesh Mehta")
EMAIL_SUBJECT_TEMPLATE = os.getenv("EMAIL_SUBJECT_TEMPLATE", "Application for {job_title} Position - {your_name}")

EMAIL_BODY_TEMPLATE = """
Dear {greeting_name},    

Applying for the {job_title} role at {company_name}, I am a B.Tech Computer Science student at VIT Bhopal (CGPA: 8.70) with advanced practical experience in full-stack development, AI, and cloud platforms. My portfolio includes impactful projects such as an AI-integrated healthcare platform, a generative storytelling AI, and scalable expense tracking solutions using technologies like React, Flask, MongoDB, and Google Gemini API.

My skill set spans Python, C++, SQL, React, Node.js, TypeScript, Flask, Scikit-learn, and more. I have delivered real-world applications deployed with CI/CD pipelines, security best practices, and robust data handling across major databases. Recognized in national hackathons and conferences, I hold certifications in Full Stack Development, Generative AI (IBM WatsonX), Cloud Computing (NPTEL), and Advanced AI (Microsoft).

I am motivated by organizations that prioritize quality, innovation, and broad impact, and am confident my technical depth and hands-on leadership will add value to {company_name}. I welcome a discussion on how my achievements and enthusiasm can contribute to your team's goals.

Best regards,
{your_name}
"""


def attach_file(message, filepath):
    """Attaches a file to the email message."""
    try:
        with open(filepath, "rb") as attachment:
            # The filename is the part of the path after the last slash
            filename = os.path.basename(filepath)
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)
            print(f"✅ Successfully attached: {filename}")
    except FileNotFoundError:
        print(f"❌ Error: Attachment file not found at '{filepath}'. Skipping this file.")
        return False
    return True


def main():
    """Main function to read CSV and send emails."""
    print("🚀 Starting Job Application Sender...")
    
    # Validate environment variables
    if not SENDER_EMAIL or not EMAIL_PASSWORD:
        print("❌ FATAL ERROR: Email credentials not found!")
        print("Please make sure SENDER_EMAIL and EMAIL_PASSWORD are set in your .env file.")
        return

    try:
        recipient_list = []
        with open(RECIPIENTS_CSV_PATH, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Skip the header line and process each data line
            for line in lines[1:]:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Split the line and find the email address
                parts = line.split()
                if len(parts) >= 4:  # Ensure we have enough parts
                    # Find the email address (contains @)
                    email_index = -1
                    for i, part in enumerate(parts):
                        if '@' in part:
                            email_index = i
                            break
                    
                    if email_index >= 2:  # Need at least SNo, Name, Email
                        # SNo is parts[0], Name is parts[1] 
                        name = parts[1]
                        email = parts[email_index]
                        
                        # Everything between name and email is additional name parts (if any)
                        if email_index > 2:
                            name_parts = parts[1:email_index]
                            name = " ".join(name_parts)
                        
                        # Everything after email is title and company combined
                        remaining_parts = parts[email_index + 1:]
                        
                        # Split remaining into title and company
                        # Assume company is last 1-2 words, title is the rest
                        if len(remaining_parts) >= 3:
                            title_parts = remaining_parts[:-2]
                            company_parts = remaining_parts[-2:]
                        elif len(remaining_parts) >= 2:
                            title_parts = remaining_parts[:-1]
                            company_parts = remaining_parts[-1:]
                        else:
                            title_parts = remaining_parts
                            company_parts = ["Unknown"]
                            
                        title = " ".join(title_parts)
                        company = " ".join(company_parts)
                        
                        recipient_list.append({
                            'Name': name,
                            'Email': email,
                            'Title': title,
                            'Company': company
                        })
                    
    except FileNotFoundError:
        print(f"❌ FATAL ERROR: The recipients file was not found at '{RECIPIENTS_CSV_PATH}'.")
        print("Please make sure the file exists and the path is correct.")
        return
    except Exception as e:
        print(f"❌ FATAL ERROR: Could not read the CSV file. Reason: {e}")
        return

    # Establish a connection to the SMTP server
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        print(f"✅ Successfully logged in to SMTP server as {SENDER_EMAIL}.")
    except Exception as e:
        print(f"❌ FATAL ERROR: Could not connect or log in to the SMTP server. Reason: {e}")
        print("Please check your email, app password, and SMTP settings.")
        return

    # Loop through each recipient and send the email
    for i, row in enumerate(recipient_list):
        # Skip the SNo column and use the new column names
        company = row['Company'].strip()
        hrname = row['Name'].strip()
        email = row['Email'].strip()
        job = row['Title'].strip()

        print("-" * 50)
        print(f"📫 Preparing email {i + 1}/{len(recipient_list)} for {company}...")

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = f"{YOUR_NAME} <{SENDER_EMAIL}>"
        msg['To'] = email

        # Format subject
        msg['Subject'] = EMAIL_SUBJECT_TEMPLATE.format(
            job_title=job,
            company_name=company,
            your_name=YOUR_NAME
        )

        # Format email body
        greeting = f" {hrname}" if hrname else "the Hiring Team"
        body = EMAIL_BODY_TEMPLATE.format(
            greeting_name=greeting,
            job_title=job,
            company_name=company,
            your_name=YOUR_NAME
        )
        msg.attach(MIMEText(body, 'plain'))

        # Attach resume and cover letter
        attach_file(msg, RESUME_FILE_PATH)
        #attach_file(msg, COVER_LETTER_PATH)

        # Send the email
        try:
            server.send_message(msg)
            print(f"✅ Email sent successfully to {email}")
        except Exception as e:
            print(f"❌ Failed to send email to {email}. Reason: {e}")

        # Wait for 10 seconds before sending the next email to avoid being flagged as spam
        if i < len(recipient_list) - 1:
            print("⏳ Waiting for 10 seconds before next email...")
            time.sleep(10)

    # Close the connection
    server.quit()
    print("-" * 50)
    print("🎉 All emails have been processed. Script finished.")


if __name__ == '__main__':
    main()
# Job Application Sender 📧

An automated Python script that sends personalized job application emails to multiple recipients with resume attachments. This tool streamlines the job application process by reading recipient data from a CSV file and sending customized emails to each hiring manager or HR representative.

## Features ✨

- **Automated Email Sending**: Send personalized emails to multiple recipients
- **CSV Integration**: Read recipient data from a structured CSV file
- **Resume Attachment**: Automatically attach your resume to each email
- **Personalized Templates**: Customize email content with recipient-specific information
- **SMTP Support**: Works with Gmail and other SMTP servers
- **Rate Limiting**: Built-in delays to avoid spam detection
- **Environment Variables**: Secure credential management with `.env` file
- **Error Handling**: Comprehensive error handling and logging

## Prerequisites 📋

- Python 3.6 or higher
- Gmail account with App Password enabled (or other SMTP server)
- Resume file in PDF format

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd job_sender
   ```

2. **Install required dependencies**:
   ```bash
   pip install python-dotenv
   ```

3. **Set up your environment variables**:
   - Copy `.env.example` to `.env` (if available) or create a new `.env` file
   - Fill in your email credentials and configuration

## Configuration ⚙️

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Email Configuration
SENDER_EMAIL=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# SMTP Server Details
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# File Paths
RESUME_FILE_PATH=your-resume.pdf
RECIPIENTS_CSV_PATH=recipient.csv

# Personal Information
YOUR_NAME=Your Full Name

# Email Templates
EMAIL_SUBJECT_TEMPLATE=Application for {job_title} Position - {your_name}
```

### Gmail App Password Setup

1. Enable 2-Factor Authentication on your Google Account
2. Go to Google Account Settings → Security → 2-Step Verification
3. Generate an App Password for "Mail"
4. Use this 16-character password in the `EMAIL_PASSWORD` field

### CSV File Format

Create a `recipient.csv` file with the following structure:

```csv
SNo,Name,Email,Title,Company
1,John Doe,john.doe@company.com,Software Engineer,Tech Corp
2,Jane Smith,jane.smith@startup.com,Frontend Developer,StartupXYZ
```

**CSV Column Requirements**:
- **SNo**: Serial number
- **Name**: Hiring manager's name
- **Email**: Recipient's email address
- **Title**: Job title you're applying for
- **Company**: Company name

## Usage 🎯

1. **Prepare your files**:
   - Place your resume PDF in the project directory
   - Create and populate the `recipient.csv` file
   - Configure your `.env` file

2. **Run the script**:
   ```bash
   python send_app.py
   ```

3. **Monitor the output**:
   - The script will show progress for each email sent
   - Success/failure status for each recipient
   - 10-second delay between emails to avoid spam detection

## Email Template 📝

The script uses a professional email template that includes:

- Personalized greeting using the recipient's name
- Job title and company name integration
- Professional introduction highlighting:
  - Educational background (B.Tech Computer Science at VIT Bhopal)
  - Technical skills and experience
  - Portfolio projects and achievements
  - Certifications and recognition
- Call to action for discussion

### Template Placeholders

The email template supports the following placeholders:
- `{greeting_name}`: Recipient's name or "the Hiring Team"
- `{job_title}`: Position being applied for
- `{company_name}`: Target company name
- `{your_name}`: Your full name

## File Structure 📁

```
job_sender/
├── send_app.py          # Main application script
├── recipient.csv        # Recipient data file
├── VikeshMehta'Resume.pdf  # Resume attachment
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
├── README.md           # This file
└── __pycache__/        # Python cache files
```

## Security Best Practices 🔒

- **Never commit `.env` file**: The `.gitignore` file excludes it from version control
- **Use App Passwords**: Don't use your main email password
- **Rotate Credentials**: Regularly update your app passwords
- **Review Recipients**: Always verify your CSV file before running the script

## Troubleshooting 🔧

### Common Issues

1. **Authentication Error**:
   - Verify your Gmail App Password is correct
   - Ensure 2FA is enabled on your Google Account
   - Check if "Less secure app access" is disabled (use App Password instead)

2. **File Not Found**:
   - Verify all file paths in `.env` are correct
   - Ensure resume and CSV files exist in the specified locations

3. **SMTP Connection Error**:
   - Check your internet connection
   - Verify SMTP server settings
   - Ensure firewall isn't blocking the connection

4. **CSV Parsing Issues**:
   - Verify CSV format matches the expected structure
   - Check for special characters in email addresses
   - Ensure no empty lines in the middle of the CSV

### Error Messages

- **"Email credentials not found!"**: Check your `.env` file configuration
- **"Attachment file not found"**: Verify resume file path and existence
- **"Could not connect to SMTP server"**: Check internet connection and SMTP settings

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer ⚠️

- Use this tool responsibly and in accordance with company application policies
- Be mindful of email frequency to avoid being marked as spam
- Always personalize your applications when possible
- This tool is for educational and personal use

## Support 💬

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review your configuration files
3. Open an issue on GitHub with detailed error information

---

**Happy Job Hunting! 🎯**
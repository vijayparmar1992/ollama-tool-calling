import json
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': 'send_email',
            'description': 'Send an email to a recipient',
            'parameters': {
                'type': 'object',
                'properties': {
                    'to': {
                        'type': 'string',
                        'description': 'Recipient email address'
                    },
                    'subject': {
                        'type': 'string',
                        'description': 'Email subject line'
                    },
                    'message': {
                        'type': 'string',
                        'description': 'Email body content'
                    }
                },
                'required': ['to', 'subject', 'message']
            }
        }
    }
]


def send_email(to: str, subject: str, message: str) -> str:
    """Send email via SMTP"""
    try:
        # Get configuration from environment variables
        smtp_host = os.getenv('SMTP_HOST', 'localhost')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))
        sender_email = os.getenv('SENDER_EMAIL', 'noreply@example.com')
        smtp_username = os.getenv('SMTP_USERNAME')
        smtp_password = os.getenv('SMTP_PASSWORD')
        
        print(f"Sending email to {to} with subject '{subject}'")
        print(f"Using SMTP: {smtp_host}:{smtp_port}")
        
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to
        msg.set_content(message)
        
        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.starttls()
            
            # Add authentication if credentials are provided
            if smtp_username and smtp_password:
                print(f"Authenticating as {smtp_username}")
                smtp.login(smtp_username, smtp_password)
            
            smtp.send_message(msg)
        
        return json.dumps({
            'status': 'success',
            'message': f'Email sent to {to}',
            'subject': subject
        })
    
    except Exception as e:
        return json.dumps({
            'status': 'error',
            'message': str(e)
        })

# Function mapping for tool execution
AVAILABLE_FUNCTIONS = {
    'send_email': send_email
}

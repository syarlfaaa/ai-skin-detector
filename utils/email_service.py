import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import GMAIL_USER, GMAIL_PASSWORD

def send_otp_email(email, otp):
    """Send OTP via email"""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = email
        msg['Subject'] = "Your OTP Code - AI Skin Detector"
        
        body = f"""
        <html>
        <head>
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    padding: 0; 
                    margin: 0;
                    background: #f5f5f5; 
                }}
                .container {{ 
                    background: white; 
                    padding: 40px; 
                    border-radius: 10px; 
                    max-width: 500px; 
                    margin: 40px auto;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                h2 {{ 
                    color: #667eea; 
                    margin-bottom: 20px;
                    text-align: center;
                }}
                .otp {{ 
                    font-size: 36px; 
                    font-weight: bold; 
                    color: #667eea; 
                    letter-spacing: 10px; 
                    background: #f0f2ff;
                    padding: 25px;
                    border-radius: 10px;
                    text-align: center;
                    margin: 30px 0;
                }}
                p {{
                    color: #666;
                    line-height: 1.6;
                    text-align: center;
                }}
                .footer {{ 
                    color: #999; 
                    font-size: 12px; 
                    margin-top: 30px;
                    text-align: center;
                    border-top: 1px solid #eee;
                    padding-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>🔐 AI Skin Detector</h2>
                <p>Hi there!</p>
                <p>Your OTP verification code is:</p>
                <div class="otp">{otp}</div>
                <p>This code will expire in <strong>5 minutes</strong>.</p>
                <p>If you didn't request this code, please ignore this email.</p>
                <div class="footer">
                    <p>This is an automated email, please do not reply.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ OTP sent successfully to {email}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False
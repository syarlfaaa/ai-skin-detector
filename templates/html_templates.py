def get_home_page():
    """Home page dengan Login & Sign Up"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Skin Detector - Login</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                min-height: 100vh;
                padding: 20px;
                position: relative;
                overflow: hidden;
            }
            
            /* Animated Background */
            .bg-animation {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            
            .face-container {
                position: absolute;
                width: 100%;
                height: 100%;
                overflow: hidden;
            }
            
            .face {
                position: absolute;
                width: 150px;
                height: 150px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 80px;
                animation: float 20s infinite ease-in-out;
            }
            
            .face:nth-child(1) {
                top: 10%;
                left: 10%;
                animation-delay: 0s;
            }
            
            .face:nth-child(2) {
                top: 60%;
                left: 80%;
                animation-delay: 3s;
            }
            
            .face:nth-child(3) {
                top: 80%;
                left: 20%;
                animation-delay: 6s;
            }
            
            .face:nth-child(4) {
                top: 30%;
                left: 70%;
                animation-delay: 9s;
            }
            
            .face:nth-child(5) {
                top: 50%;
                left: 5%;
                animation-delay: 12s;
            }
            
            @keyframes float {
                0%, 100% {
                    transform: translate(0, 0) rotate(0deg);
                }
                25% {
                    transform: translate(30px, -30px) rotate(5deg);
                }
                50% {
                    transform: translate(-20px, 20px) rotate(-5deg);
                }
                75% {
                    transform: translate(20px, 30px) rotate(3deg);
                }
            }
            
            .container {
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: calc(100vh - 40px);
            }
            
            .login-box {
                background: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                width: 100%;
                max-width: 400px;
                backdrop-filter: blur(10px);
            }
            
            h2 {
                text-align: center;
                color: #333;
                margin-bottom: 10px;
                font-size: 28px;
            }
            
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
                font-size: 14px;
            }
            
            .tabs {
                display: flex;
                margin-bottom: 25px;
                border-bottom: 2px solid #f0f0f0;
            }
            
            .tab {
                flex: 1;
                text-align: center;
                padding: 12px;
                cursor: pointer;
                color: #999;
                font-weight: 500;
                transition: all 0.3s;
                position: relative;
            }
            
            .tab.active {
                color: #667eea;
            }
            
            .tab.active::after {
                content: '';
                position: absolute;
                bottom: -2px;
                left: 0;
                right: 0;
                height: 2px;
                background: #667eea;
            }
            
            .form-container {
                display: none;
            }
            
            .form-container.active {
                display: block;
                animation: fadeIn 0.3s;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .input-group {
                margin-bottom: 20px;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
                color: #555;
                font-size: 14px;
                font-weight: 500;
            }
            
            input {
                width: 100%;
                padding: 12px 15px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                font-size: 15px;
                transition: all 0.3s;
            }
            
            input:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            
            button {
                width: 100%;
                padding: 14px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                transition: all 0.3s;
                margin-top: 10px;
            }
            
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            
            button:active {
                transform: translateY(0);
            }
            
            .icon {
                font-size: 48px;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="bg-animation">
            <div class="face-container">
                <div class="face">😊</div>
                <div class="face">🌟</div>
                <div class="face">✨</div>
                <div class="face">💆</div>
                <div class="face">🧴</div>
            </div>
        </div>
        
        <div class="container">
            <div class="login-box">
                <div class="icon">🔐</div>
                <h2>AI Skin Detector</h2>
                <p class="subtitle">Detect your skin type & get recommendations</p>
                
                <div class="tabs">
                    <div class="tab active" onclick="showForm('login')">Login</div>
                    <div class="tab" onclick="showForm('signup')">Sign Up</div>
                </div>
                
                <!-- Login Form -->
                <div id="login" class="form-container active">
                    <form action="/login" method="post">
                        <div class="input-group">
                            <label>Email</label>
                            <input type="email" name="email" placeholder="your@email.com" required>
                        </div>
                        <div class="input-group">
                            <label>Password</label>
                            <input type="password" name="password" placeholder="Enter your password" required>
                        </div>
                        <button type="submit">Login</button>
                    </form>
                </div>
                
                <!-- Sign Up Form -->
                <div id="signup" class="form-container">
                    <form action="/signup" method="post">
                        <div class="input-group">
                            <label>Full Name</label>
                            <input type="text" name="name" placeholder="John Doe" required>
                        </div>
                        <div class="input-group">
                            <label>Email</label>
                            <input type="email" name="email" placeholder="your@email.com" required>
                        </div>
                        <div class="input-group">
                            <label>Password</label>
                            <input type="password" name="password" placeholder="Create a password" required minlength="6">
                        </div>
                        <button type="submit">Send OTP</button>
                    </form>
                </div>
            </div>
        </div>
        
        <script>
            function showForm(formId) {
                document.querySelectorAll('.form-container').forEach(form => {
                    form.classList.remove('active');
                });
                document.querySelectorAll('.tab').forEach(tab => {
                    tab.classList.remove('active');
                });
                document.getElementById(formId).classList.add('active');
                event.target.classList.add('active');
            }
        </script>
    </body>
    </html>
    """

def get_error_page(title, message):
    """Generic error page"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .message-box {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 400px;
            }}
            h2 {{ color: #e74c3c; margin-bottom: 20px; }}
            p {{ color: #666; margin-bottom: 25px; }}
            a {{
                display: inline-block;
                padding: 12px 30px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: all 0.3s;
            }}
            a:hover {{ background: #5568d3; }}
        </style>
    </head>
    <body>
        <div class="message-box">
            <h2>❌ {title}</h2>
            <p>{message}</p>
            <a href="/">Back to Login</a>
        </div>
    </body>
    </html>
    """

def get_otp_verification_page(email):
    """OTP verification page"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Verify OTP</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
                width: 100%;
                max-width: 400px;
                text-align: center;
            }}
            h2 {{ color: #333; margin-bottom: 15px; }}
            .icon {{ font-size: 64px; margin-bottom: 20px; }}
            p {{ color: #666; margin-bottom: 15px; line-height: 1.6; }}
            .email {{ 
                background: #f8f9fa;
                padding: 10px 15px;
                border-radius: 8px;
                color: #667eea;
                font-weight: bold;
                margin: 20px 0;
            }}
            input {{
                width: 100%;
                padding: 15px;
                margin: 20px 0;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                box-sizing: border-box;
                text-align: center;
                font-size: 24px;
                letter-spacing: 8px;
                font-weight: bold;
            }}
            input:focus {{
                outline: none;
                border-color: #667eea;
            }}
            button {{
                width: 100%;
                padding: 14px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                transition: all 0.3s;
            }}
            button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="icon">📧</div>
            <h2>Verify Your Email</h2>
            <p>We've sent a 6-digit OTP code to:</p>
            <div class="email">{email}</div>
            <p>Please check your email and enter the code below:</p>
            <form action="/verify-otp" method="post">
                <input type="hidden" name="email" value="{email}">
                <input type="text" name="otp" placeholder="000000" maxlength="6" pattern="[0-9]{{6}}" required autofocus>
                <button type="submit">Verify OTP</button>
            </form>
        </div>
    </body>
    </html>
    """

def get_success_page(name, email):
    """Success registration page"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign Up Success</title>
        <meta http-equiv="refresh" content="3;url=/">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .message-box {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 400px;
            }}
            h2 {{ color: #27ae60; margin-bottom: 20px; }}
            .icon {{ font-size: 64px; margin-bottom: 20px; }}
            p {{ color: #666; margin-bottom: 15px; }}
            .email {{ 
                background: #f8f9fa;
                padding: 10px 15px;
                border-radius: 8px;
                color: #667eea;
                font-weight: bold;
                margin: 20px 0;
            }}
            .spinner {{
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 20px auto;
            }}
            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
        </style>
    </head>
    <body>
        <div class="message-box">
            <div class="icon">✅</div>
            <h2>Account Created!</h2>
            <p>Welcome, <strong>{name}</strong>!</p>
            <div class="email">{email}</div>
            <p>Your account has been successfully created.</p>
            <p>Redirecting to login page...</p>
            <div class="spinner"></div>
        </div>
    </body>
    </html>
    """
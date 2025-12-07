from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import random
from utils.database import load_users, save_users
from utils.email_service import send_otp_email
from templates.html_templates import (
    get_error_page, 
    get_otp_verification_page, 
    get_success_page
)
from config import OTP_STORE, GRADIO_URL

router = APIRouter()

@router.post("/signup")
async def signup(name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    """Handle sign up - Send OTP"""
    users = load_users()
    
    # Check if email already exists
    if email in users:
        return HTMLResponse(get_error_page(
            "Email Already Registered!",
            "This email is already in use. Please login instead."
        ))
    
    # Generate 6-digit OTP
    otp = str(random.randint(100000, 999999))
    
    # Store OTP temporarily
    OTP_STORE[email] = {
        'otp': otp,
        'name': name,
        'password': password
    }
    
    print(f"📧 Sending OTP {otp} to {email}...")
    
    # Send OTP via email
    if send_otp_email(email, otp):
        return HTMLResponse(get_otp_verification_page(email))
    else:
        return HTMLResponse(get_error_page(
            "Failed to Send OTP!",
            "There was an error sending the OTP. Please try again."
        ))


@router.post("/verify-otp")
async def verify_otp(email: str = Form(...), otp: str = Form(...)):
    """Verify OTP and create account"""
    
    # Check if OTP exists
    if email not in OTP_STORE:
        return HTMLResponse(get_error_page(
            "OTP Expired!",
            "Your OTP has expired. Please sign up again."
        ))
    
    stored_data = OTP_STORE[email]
    
    # Verify OTP
    if stored_data['otp'] == otp:
        # OTP is correct - Save user
        users = load_users()
        users[email] = {
            'name': stored_data['name'],
            'password': stored_data['password']
        }
        save_users(users)
        
        # Clear OTP from memory
        del OTP_STORE[email]
        
        print(f"✅ User {email} registered successfully!")
        
        # Success - redirect to login
        return HTMLResponse(get_success_page(stored_data['name'], email))
    else:
        # Wrong OTP
        return HTMLResponse(get_error_page(
            "Invalid OTP!",
            "The OTP code you entered is incorrect. Please check your email and try again."
        ))


@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    """Handle login"""
    users = load_users()
    
    # Check credentials
    if email in users and users[email]['password'] == password:
        # Success - redirect to Knowledge page first
        print(f"✅ User {email} logged in successfully!")
        return RedirectResponse(url="/knowledge", status_code=303)
    else:
        # Failed
        return HTMLResponse(get_error_page(
            "Login Failed!",
            "Invalid email or password."
        ))
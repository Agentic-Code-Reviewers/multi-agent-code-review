import os
import sqlite3
import requests
import subprocess
import ipaddress

# ❌ VULNERABILITY 1: Hardcoded Sensitive Information (CWE-798 / OWASP A07)
# Real API keys or passwords should never be committed to code.
STRIPE_API_KEY = ""

def get_db_connection():
    return sqlite3.connect('users.db')

def get_user_profile(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # ✅ Fixed: Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    user = cursor.fetchone()
    conn.close()
    return user

def ping_host(user_input_ip):
    # ✅ Fixed: Validate IP format and avoid shell by using subprocess.run with list
    try:
        ipaddress.ip_address(user_input_ip)
    except ValueError:
        raise ValueError("Invalid IP address")
    
    subprocess.run(['ping', '-c', '1', user_input_ip])

if __name__ == "__main__":
    # Test execution
    user = get_user_profile("admin' OR '1'='1")  # SQLi test payload (now safe)
    ping_host("8.8.8.8; cat /etc/passwd")        # Command Injection test payload (now safe: raises ValueError or does not execute shell)

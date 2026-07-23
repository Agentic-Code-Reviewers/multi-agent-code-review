"""Test application with intentional code issues for agent testing.

This file contains:
- Security issues (SQL injection, hardcoded secrets)
- Bug detection issues (undefined variables, type mismatches)
- Style issues (poor naming, inconsistent formatting)
- Performance issues (inefficient algorithms, unnecessary loops)
"""

import pickle
import os
import subprocess
from datetime import datetime


# ============================================================
# SECURITY ISSUES
# ============================================================

def authenticate_user(username, password):
    """SQL Injection vulnerability."""
    import sqlite3
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # SECURITY BUG: SQL Injection - user input directly concatenated
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    return cursor.fetchone()


def fetch_data_from_api(url):
    """Hardcoded credentials and unvalidated shell execution."""
    # SECURITY BUG: Hardcoded API key (example format)
    api_key = "sk_XXXX_HARDCODED_SECRET_DETECTED"
    
    # SECURITY BUG: Command injection - url not sanitized
    result = subprocess.run(f"curl {url}", shell=True, capture_output=True)
    return result.stdout


def deserialize_user_data(data):
    """Unsafe deserialization."""
    # SECURITY BUG: pickle.loads() on untrusted data
    return pickle.loads(data)


def log_user_action(user_id, action):
    """Information disclosure."""
    # SECURITY BUG: Sensitive data in logs
    github_token = os.environ.get('GITHUB_TOKEN')
    with open('/tmp/user_actions.log', 'a') as f:
        f.write(f"User {user_id} performed {action} with token {github_token}\n")


# ============================================================
# BUG DETECTION ISSUES
# ============================================================

def calculate_total(items):
    """Undefined variable bug."""
    # BUG: 'total' is used before being defined
    for item in items:
        total += item['price']
    return total


def process_user_data(user_dict):
    """Type mismatch and attribute error."""
    # BUG: Treating string as dict
    name = user_dict['name']
    age = user_dict['age']
    
    # BUG: Trying to call string method on potential None
    email = user_dict.get('email')
    domain = email.split('@')[1]
    
    return f"{name} ({age}): {domain}"


def divide_numbers(a, b):
    """Division by zero."""
    # BUG: No check for b == 0
    return a / b


def read_file_unsafe(filename):
    """File handling without proper error handling."""
    # BUG: No try-except, file may not exist
    with open(filename) as f:
        return f.read()


# ============================================================
# STYLE ISSUES
# ============================================================

def x(a,b,c):
    """Poor naming and formatting."""
    # STYLE: Single-letter variable names, no spacing
    r=a+b+c
    return r


class MyClass:
    """Inconsistent naming conventions."""
    
    def __init__(self):
        self.myVar = 1
        self.MY_VAR_2 = 2
        self._privateStuff = 3
    
    def do_something(self):
        """Method with no docstring."""
        pass
    
    def DoAnotherThing(self):
        """Inconsistent naming: PascalCase instead of snake_case."""
        pass


def long_line_function():
    """Line too long and too many statements on one line."""
    x = 1; y = 2; z = 3; result = x + y + z; print(result); return result  # This is way too long and has multiple statements


# ============================================================
# PERFORMANCE ISSUES
# ============================================================

def find_duplicate_inefficient(items):
    """O(n²) algorithm when O(n) is possible."""
    duplicates = []
    # PERFORMANCE: Nested loops - inefficient O(n²)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates


def fibonacci_recursive(n):
    """Exponential time complexity."""
    # PERFORMANCE: Recursive without memoization - O(2^n)
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def process_list_inefficient(data):
    """Creating unnecessary copies and intermediate lists."""
    # PERFORMANCE: Multiple unnecessary iterations and list copies
    result = []
    for item in data:
        if item > 0:
            result.append(item)
    
    # PERFORMANCE: Creating intermediate list, then filtering again
    filtered = [x for x in result if x < 100]
    
    # PERFORMANCE: Another unnecessary loop
    final = []
    for x in filtered:
        final.append(x * 2)
    
    return final


def memory_leak_potential():
    """Potential memory leak with growing list."""
    cache = []
    # PERFORMANCE: Growing list without bounds
    def add_to_cache(item):
        cache.append(item)
        return cache
    
    return add_to_cache


# ============================================================
# MIXED ISSUES
# ============================================================

def unsafe_database_operation(user_id, user_input):
    """Combines multiple issues."""
    import sqlite3
    
    # BUG: No type checking
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # SECURITY: SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE id={user_id} AND query LIKE '%{user_input}%'")
    
    # PERFORMANCE: Fetching all rows when might only need one
    rows = cursor.fetchall()
    
    # BUG: IndexError if no rows returned
    return rows[0]


if __name__ == "__main__":
    # SECURITY: Hardcoded secret (should use env vars instead)
    SECRET = "password_XXXX_should_use_env_vars"
    
    # This is test code
    print("This file contains intentional issues for testing the multi-agent code review system")

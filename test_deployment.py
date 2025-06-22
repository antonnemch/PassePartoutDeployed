#!/usr/bin/env python3
"""
Test script to verify Vercel deployment
"""

import requests
import json
import os

def test_deployment():
    """Test the deployed backend endpoints"""
    
    # Get the base URL from environment or use a default
    base_url = os.getenv('VERCEL_URL', 'https://passepartout-deployed.vercel.app')
    if not base_url.startswith('http'):
        base_url = f'https://{base_url}'
    
    print(f"Testing deployment at: {base_url}")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"Response: {response.json()}")
        else:
            print("❌ Health check failed")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"Root endpoint: {response.status_code}")
        if response.status_code == 200:
            print("✅ Root endpoint passed")
            print(f"Response: {response.json()}")
        else:
            print("❌ Root endpoint failed")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    
    # Test route generation endpoint
    try:
        test_request = {
            "input_text": "I want a 2km walk starting at CN Tower",
            "context": None
        }
        response = requests.post(
            f"{base_url}/generate-route", 
            json=test_request,
            timeout=30
        )
        print(f"Route generation: {response.status_code}")
        if response.status_code == 200:
            print("✅ Route generation passed")
            data = response.json()
            print(f"Route points: {len(data.get('route', {}).get('points', []))}")
        else:
            print("❌ Route generation failed")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Route generation error: {e}")

if __name__ == "__main__":
    test_deployment() 
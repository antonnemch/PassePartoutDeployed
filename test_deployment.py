#!/usr/bin/env python3
"""
Test script to verify deployment configuration
"""

import requests
import json
import os
from datetime import datetime

def test_backend_health(base_url):
    """Test backend health endpoint"""
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"✅ Health check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Status: {data.get('status')}")
            print(f"   Timestamp: {data.get('timestamp')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_root_endpoint(base_url):
    """Test root endpoint"""
    try:
        response = requests.get(base_url, timeout=10)
        print(f"✅ Root endpoint: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Message: {data.get('message')}")
            print(f"   Environment: {data.get('environment')}")
            print(f"   Endpoints: {list(data.get('endpoints', {}).keys())}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
        return False

def test_route_generation(base_url):
    """Test route generation endpoint"""
    try:
        payload = {
            "input_text": "I want a 2km walk starting at CN Tower",
            "context": None
        }
        response = requests.post(
            f"{base_url}/generate-route", 
            json=payload, 
            timeout=30
        )
        print(f"✅ Route generation: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Success: {data.get('success')}")
            print(f"   Route distance: {data.get('total_distance_km', 'N/A')}km")
            print(f"   Points: {len(data.get('points', []))}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Route generation failed: {e}")
        return False

def test_roam_endpoint(base_url):
    """Test roam endpoint"""
    try:
        payload = {
            "coordinates": "43.6426, -79.3871",
            "context": None
        }
        response = requests.post(
            f"{base_url}/roam", 
            json=payload, 
            timeout=30
        )
        print(f"✅ Roam endpoint: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Summary length: {len(data.get('summary', ''))}")
            print(f"   Location: {data.get('location', 'N/A')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Roam endpoint failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing EarSightAI Backend Deployment")
    print("=" * 50)
    
    # Test URLs
    urls = [
        "http://localhost:8000",
        "https://passepartout-deployed.vercel.app/api"
    ]
    
    for url in urls:
        print(f"\n📍 Testing: {url}")
        print("-" * 30)
        
        # Test basic endpoints
        health_ok = test_backend_health(url)
        root_ok = test_root_endpoint(url)
        
        if health_ok and root_ok:
            # Test functional endpoints
            route_ok = test_route_generation(url)
            roam_ok = test_roam_endpoint(url)
            
            print(f"\n📊 Results for {url}:")
            print(f"   Health: {'✅' if health_ok else '❌'}")
            print(f"   Root: {'✅' if root_ok else '❌'}")
            print(f"   Route: {'✅' if route_ok else '❌'}")
            print(f"   Roam: {'✅' if roam_ok else '❌'}")
        else:
            print(f"\n❌ Basic endpoints failed for {url}")
    
    print("\n🎯 Deployment Test Complete!")

if __name__ == "__main__":
    main() 
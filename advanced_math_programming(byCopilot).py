#!/usr/bin/env python3
"""
Amazing Mathematical Concepts in Programming
A journey through the hidden math that powers technology
"""

import math
import time
import random

print("🌟 AMAZING MATH IN PROGRAMMING: YOUR NEXT ADVENTURE!")
print("=" * 65)

def fourier_transforms_magic():
    """Explore how Fourier transforms power digital technology"""
    print("🎵 FOURIER TRANSFORMS: THE MATH BEHIND SOUND & IMAGES")
    print("-" * 55)
    
    print("💡 THE BIG IDEA:")
    print("   Any signal can be broken down into sine waves!")
    print("   Music, images, WiFi, JPEGs - all use this math!")
    print()
    
    print("🎼 EXAMPLE: Musical Note Analysis")
    print("   A piano chord = sum of pure sine waves")
    print("   Your phone 'hears' each frequency separately")
    print()
    
    # Simple demonstration
    def create_signal(frequencies, amplitudes, time_points):
        """Create a signal from multiple frequencies"""
        signal = []
        for t in time_points:
            value = 0
            for freq, amp in zip(frequencies, amplitudes):
                value += amp * math.sin(2 * math.pi * freq * t)
            signal.append(value)
        return signal
    
    # Create a simple signal (like a musical chord)
    time_points = [i/100 for i in range(50)]  # 0.5 seconds at 100Hz
    frequencies = [440, 554, 659]  # A major chord (A, C#, E)
    amplitudes = [1, 0.8, 0.6]
    
    signal = create_signal(frequencies, amplitudes, time_points)
    
    print("🎹 Musical Chord Simulation:")
    print("   Frequencies: 440Hz (A), 554Hz (C#), 659Hz (E)")
    print("   Combined signal (first 10 samples):")
    for i, sample in enumerate(signal[:10]):
        print(f"   t={time_points[i]:.2f}s: {sample:6.3f}")
    
    print()
    print("🎯 REAL-WORLD APPLICATIONS:")
    applications = [
        ("📱 MP3 Compression", "Remove frequencies humans can't hear"),
        ("📷 JPEG Images", "Compress by removing high-frequency details"),
        ("📡 WiFi/Bluetooth", "Separate different signal channels"),
        ("🎮 Audio Processing", "Real-time effects in games/music apps"),
        ("🏥 Medical Imaging", "MRI, CT scans use Fourier analysis"),
        ("📺 Digital TV", "Compress video signals for transmission")
    ]
    
    for app, description in applications:
        print(f"   {app}: {description}")

def machine_learning_math():
    """Explore the math behind AI and machine learning"""
    print("\n🧠 MACHINE LEARNING: THE MATH BEHIND AI")
    print("-" * 45)
    
    print("💡 THE SECRET: It's all about finding patterns in data!")
    print("   And the math is surprisingly approachable!")
    print()
    
    print("📈 LINEAR REGRESSION (simplest ML):")
    print("   Find the best line through data points")
    print("   Formula: y = mx + b")
    print("   Goal: Find 'm' and 'b' that minimize errors")
    print()
    
    # Simple linear regression example
    def simple_linear_regression(x_data, y_data):
        """Find best fit line through data points"""
        n = len(x_data)
        sum_x = sum(x_data)
        sum_y = sum(y_data)
        sum_xy = sum(x * y for x, y in zip(x_data, y_data))
        sum_x2 = sum(x * x for x in x_data)
        
        # Calculate slope (m) and intercept (b)
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
        b = (sum_y - m * sum_x) / n
        
        return m, b
    
    # Example: Predict house prices based on size
    house_sizes = [1000, 1200, 1400, 1600, 1800, 2000]  # sq ft
    house_prices = [200, 240, 280, 320, 360, 400]       # thousands
    
    slope, intercept = simple_linear_regression(house_sizes, house_prices)
    
    print("🏠 HOUSE PRICE PREDICTION EXAMPLE:")
    print(f"   Formula: price = {slope:.3f} × size + {intercept:.1f}")
    print("   Data points:")
    for size, price in zip(house_sizes, house_prices):
        predicted = slope * size + intercept
        print(f"   {size} sq ft → ${price}k (predicted: ${predicted:.1f}k)")
    
    print()
    print("🤖 MORE ADVANCED ML CONCEPTS:")
    concepts = [
        ("🧮 Calculus", "Gradient descent finds minimum error"),
        ("📊 Statistics", "Probability distributions in data"),
        ("🔢 Linear Algebra", "Vectors and matrices for data"),
        ("🎯 Optimization", "Finding best parameters automatically"),
        ("📈 Derivatives", "How to improve predictions step by step")
    ]
    
    for concept, description in concepts:
        print(f"   {concept}: {description}")

def graphics_and_3d_math():
    """Explore 3D graphics and computer vision"""
    print("\n🎮 3D GRAPHICS: THE MATH BEHIND VIRTUAL WORLDS")
    print("-" * 50)
    
    print("💡 EVERY 3D GAME uses these mathematical concepts!")
    print()
    
    print("📐 CORE CONCEPTS:")
    
    # Vector operations
    def vector_add(v1, v2):
        return [v1[i] + v2[i] for i in range(len(v1))]
    
    def vector_dot(v1, v2):
        return sum(v1[i] * v2[i] for i in range(len(v1)))
    
    def vector_length(v):
        return math.sqrt(sum(x*x for x in v))
    
    # Example: 3D point manipulation
    point_a = [1, 2, 3]  # 3D coordinates
    point_b = [4, 1, 2]
    
    print("🎯 VECTOR OPERATIONS:")
    print(f"   Point A: {point_a}")
    print(f"   Point B: {point_b}")
    print(f"   A + B = {vector_add(point_a, point_b)}")
    print(f"   Dot product = {vector_dot(point_a, point_b)}")
    print(f"   Distance from origin = {vector_length(point_a):.2f}")
    print()
    
    print("🔄 ROTATION MATHEMATICS:")
    def rotate_2d(x, y, angle_degrees):
        """Rotate a 2D point around origin"""
        angle_rad = math.radians(angle_degrees)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        new_x = x * cos_a - y * sin_a
        new_y = x * sin_a + y * cos_a
        return new_x, new_y
    
    # Rotate a point
    original = (3, 4)
    rotated_45 = rotate_2d(3, 4, 45)
    rotated_90 = rotate_2d(3, 4, 90)
    
    print(f"   Original point: {original}")
    print(f"   Rotated 45°: ({rotated_45[0]:.2f}, {rotated_45[1]:.2f})")
    print(f"   Rotated 90°: ({rotated_90[0]:.2f}, {rotated_90[1]:.2f})")
    print()
    
    print("🌟 APPLICATIONS:")
    apps = [
        ("🎮 Video Games", "Character movement, camera control"),
        ("🎬 Movies", "CGI effects, animation"),
        ("🏗️ Architecture", "3D building design"),
        ("🚗 Car Design", "Aerodynamics simulation"),
        ("📱 AR/VR", "Virtual reality environments"),
        ("🎯 Navigation", "GPS route calculation")
    ]
    
    for app, description in apps:
        print(f"   {app}: {description}")

def cryptography_math():
    """Explore the math behind internet security"""
    print("\n🔐 CRYPTOGRAPHY: THE MATH PROTECTING YOUR DATA")
    print("-" * 50)
    
    print("💡 EVERY TIME you browse the web, buy online, or send")
    print("   a message, cryptographic math protects you!")
    print()
    
    print("🔢 RSA ENCRYPTION (simplified concept):")
    print("   Based on the fact that multiplying is easy,")
    print("   but factoring large numbers is VERY hard!")
    print()
    
    # Simple demonstration with small numbers
    def simple_rsa_demo():
        """Demonstrate RSA concept with small numbers"""
        # Choose two small primes (in real RSA, these are HUGE)
        p, q = 7, 11
        n = p * q  # This would be ~2048 bits in real RSA
        
        print(f"🎯 RSA DEMO (simplified):")
        print(f"   Two secret primes: p={p}, q={q}")
        print(f"   Public modulus: n = p×q = {n}")
        print(f"   Finding p and q from {n} is the hard problem!")
        print()
        
        # Show factorization difficulty
        print("   For small numbers, factoring is easy:")
        print(f"   {n} = {p} × {q}")
        print()
        print("   But for REAL RSA:")
        print("   n has ~600 decimal digits")
        print("   Finding its factors would take billions of years!")
        
    simple_rsa_demo()
    
    print("\n🧮 OTHER CRYPTO MATH:")
    crypto_concepts = [
        ("🔄 Modular Arithmetic", "Clock math for key operations"),
        ("🔢 Prime Numbers", "Foundation of public key crypto"),
        ("📐 Elliptic Curves", "More efficient than RSA"),
        ("🎲 Hash Functions", "One-way mathematical functions"),
        ("🔐 Symmetric Encryption", "Fast algorithms like AES")
    ]
    
    for concept, description in crypto_concepts:
        print(f"   {concept}: {description}")

def suggest_next_topics():
    """Suggest fascinating areas to explore next"""
    print("\n🚀 YOUR NEXT MATHEMATICAL ADVENTURES")
    print("-" * 45)
    
    topics = [
        ("🎮 Game Theory", "Strategic thinking, AI behavior, economics"),
        ("🌊 Chaos Theory", "Weather prediction, population dynamics"),
        ("📊 Information Theory", "Data compression, communication efficiency"),
        ("🧬 Computational Biology", "DNA analysis, protein folding"),
        ("🌌 Computational Physics", "Simulating galaxies, quantum mechanics"),
        ("🎨 Computer Graphics", "Ray tracing, 3D modeling, animation"),
        ("🔊 Digital Signal Processing", "Audio/video processing, filters"),
        ("🤖 Neural Networks", "Deep learning, artificial intelligence"),
        ("📈 Optimization Theory", "Finding best solutions efficiently"),
        ("🔍 Computer Vision", "Image recognition, autonomous vehicles")
    ]
    
    print("Fascinating areas where math meets programming:")
    print()
    for topic, description in topics:
        print(f"{topic}: {description}")
    
    print()
    print("🎯 PICK ONE that interests you and we can explore it!")
    print("Each area has its own beautiful mathematical foundations!")

# Run all demonstrations
if __name__ == "__main__":
    fourier_transforms_magic()
    machine_learning_math()
    graphics_and_3d_math()
    cryptography_math()
    suggest_next_topics()
    
    print("\n" + "=" * 65)
    print("🌟 THE AMAZING TRUTH ABOUT MATH IN PROGRAMMING")
    print("=" * 65)
    
    print("💡 EVERY app, game, website, and digital device")
    print("   is powered by hundreds of mathematical concepts!")
    print()
    print("🎭 The 'magic' of technology is really mathematics")
    print("   disguised so well that it feels like magic!")
    print()
    print("🚀 Whether you realize it or not, every programmer")
    print("   is really an applied mathematician!")
    print()
    print("🌈 Mathematics isn't just about solving equations -")
    print("   it's about understanding patterns, solving problems,")
    print("   and creating digital worlds!")
    print()
    print("🎯 Pick any topic that excited you and dive deeper!")
    print("   The rabbit hole of mathematical programming")
    print("   goes infinitely deep... and it's all fascinating! ✨")

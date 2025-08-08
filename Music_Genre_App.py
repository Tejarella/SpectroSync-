<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpectroSync - AI Music Genre Classification</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --primary-bg: #0a0a0f;
            --secondary-bg: #1a1a2e;
            --accent-green: #00ff88;
            --accent-cyan: #00d4ff;
            --glass-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-primary: #ffffff;
            --text-secondary: #b8b8d1;
            --gradient-primary: linear-gradient(135deg, #00ff88, #00d4ff);
            --gradient-secondary: linear-gradient(135deg, #1a1a2e, #16213e);
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: var(--primary-bg);
            color: var(--text-primary);
            overflow-x: hidden;
            min-height: 100vh;
        }
        
        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.3;
            pointer-events: none;
        }
        
        .particle {
            position: absolute;
            width: 2px;
            height: 2px;
            background: var(--accent-green);
            border-radius: 50%;
            animation: float 8s infinite linear;
        }
        
        @keyframes float {
            0% { 
                transform: translateY(100vh) translateX(0px) rotate(0deg);
                opacity: 0;
            }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { 
                transform: translateY(-10px) translateX(100px) rotate(360deg);
                opacity: 0;
            }
        }
        
        /* Sidebar */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 280px;
            height: 100vh;
            background: rgba(26, 26, 46, 0.9);
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--glass-border);
            padding: 2rem 0;
            z-index: 1000;
            transition: transform 0.3s ease;
        }
        
        .logo {
            text-align: center;
            margin-bottom: 3rem;
            padding: 0 2rem;
        }
        
        .logo h1 {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 1.8rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .logo p {
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
            letter-spacing: 2px;
        }
        
        .nav-menu {
            list-style: none;
            padding: 0 1rem;
        }
        
        .nav-item {
            margin-bottom: 1rem;
        }
        
        .nav-link {
            display: flex;
            align-items: center;
            padding: 1rem 1.5rem;
            color: var(--text-secondary);
            text-decoration: none;
            border-radius: 15px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .nav-link:hover, .nav-link.active {
            color: var(--text-primary);
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            transform: translateX(5px);
        }
        
        .nav-link i {
            margin-right: 1rem;
            font-size: 1.2rem;
            width: 20px;
        }
        
        /* Main Content */
        .main-content {
            margin-left: 280px;
            min-height: 100vh;
            padding: 2rem 3rem;
            transition: margin-left 0.3s ease;
        }
        
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
        }
        
        .menu-toggle {
            display: none;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            padding: 0.8rem;
            border-radius: 10px;
            cursor: pointer;
            backdrop-filter: blur(10px);
        }
        
        .page-title {
            font-family: 'Orbitron', monospace;
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Glass Cards */
        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            transition: all 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 255, 136, 0.1);
        }
        
        /* Buttons */
        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
            gap: 0.5rem;
        }
        
        .btn-primary {
            background: var(--gradient-primary);
            color: white;
            box-shadow: 0 5px 15px rgba(0, 255, 136, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 255, 136, 0.4);
        }
        
        .btn-secondary {
            background: var(--glass-bg);
            color: var(--text-primary);
            border: 1px solid var(--glass-border);
            backdrop-filter: blur(10px);
        }
        
        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }
        
        /* File Upload */
        .upload-area {
            border: 2px dashed var(--accent-green);
            border-radius: 20px;
            padding: 3rem;
            text-align: center;
            background: rgba(0, 255, 136, 0.05);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .upload-area:hover {
            border-color: var(--accent-cyan);
            background: rgba(0, 212, 255, 0.05);
            transform: scale(1.02);
        }
        
        .upload-area.dragover {
            border-color: var(--accent-cyan);
            background: rgba(0, 212, 255, 0.1);
            transform: scale(1.05);
        }
        
        .upload-icon {
            font-size: 3rem;
            color: var(--accent-green);
            margin-bottom: 1rem;
        }
        
        .file-input {
            display: none;
        }
        
        /* Audio Player */
        .audio-player {
            background: var(--glass-bg);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
        }
        
        .audio-visualizer {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 60px;
            margin-bottom: 1rem;
            gap: 3px;
        }
        
        .bar {
            width: 4px;
            background: var(--gradient-primary);
            border-radius: 2px;
            animation: pulse 1.5s infinite ease-in-out;
            animation-play-state: paused;
        }
        
        .bar:nth-child(1) { animation-delay: 0s; height: 20px; }
        .bar:nth-child(2) { animation-delay: 0.1s; height: 30px; }
        .bar:nth-child(3) { animation-delay: 0.2s; height: 40px; }
        .bar:nth-child(4) { animation-delay: 0.3s; height: 50px; }
        .bar:nth-child(5) { animation-delay: 0.4s; height: 40px; }
        .bar:nth-child(6) { animation-delay: 0.5s; height: 30px; }
        .bar:nth-child(7) { animation-delay: 0.6s; height: 20px; }
        .bar:nth-child(8) { animation-delay: 0.7s; height: 25px; }
        
        @keyframes pulse {
            0%, 100% { transform: scaleY(0.3); opacity: 0.7; }
            50% { transform: scaleY(1); opacity: 1; }
        }
        
        /* Results */
        .result-card {
            background: var(--gradient-secondary);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            border: 1px solid var(--glass-border);
            position: relative;
            overflow: hidden;
        }
        
        .result-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.2), transparent);
            animation: shimmer 2s infinite;
        }
        
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        .genre-result {
            font-family: 'Orbitron', monospace;
            font-size: 2rem;
            font-weight: 700;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 1rem 0;
        }
        
        /* Loading Spinner */
        .loading {
            display: none;
            text-align: center;
            padding: 2rem;
        }
        
        .spinner {
            width: 60px;
            height: 60px;
            border: 3px solid var(--glass-border);
            border-top: 3px solid var(--accent-green);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Wave Animation */
        .wave-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
            gap: 4px;
        }
        
        .wave {
            width: 5px;
            height: 20px;
            background: var(--gradient-primary);
            border-radius: 3px;
            animation: wave 1.2s ease-in-out infinite;
        }
        
        .wave:nth-child(1) { animation-delay: 0s; }
        .wave:nth-child(2) { animation-delay: 0.1s; }
        .wave:nth-child(3) { animation-delay: 0.2s; }
        .wave:nth-child(4) { animation-delay: 0.3s; }
        .wave:nth-child(5) { animation-delay: 0.4s; }
        
        @keyframes wave {
            0%, 40%, 100% { transform: scaleY(0.4); }
            20% { transform: scaleY(1.2); }
        }
        
        /* Page Content */
        .page {
            display: none;
            animation: fadeIn 0.5s ease-in;
        }
        
        .page.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .hero-section {
            text-align: center;
            padding: 4rem 2rem;
            background: var(--gradient-secondary);
            border-radius: 30px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .hero-content {
            position: relative;
            z-index: 2;
        }
        
        .hero-title {
            font-family: 'Orbitron', monospace;
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .feature-card {
            background: var(--glass-bg);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            border: 1px solid var(--glass-border);
            backdrop-filter: blur(20px);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 255, 136, 0.2);
        }
        
        .feature-icon {
            font-size: 3rem;
            color: var(--accent-green);
            margin-bottom: 1rem;
        }
        
        .about-content {
            line-height: 1.8;
            font-size: 1.1rem;
        }
        
        .about-content h3 {
            color: var(--accent-green);
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-family: 'Orbitron', monospace;
        }
        
        .genre-list {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .genre-tag {
            background: var(--gradient-primary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: 600;
            font-size: 0.9rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .sidebar {
                transform: translateX(-100%);
            }
            
            .sidebar.active {
                transform: translateX(0);
            }
            
            .main-content {
                margin-left: 0;
                padding: 1rem 1.5rem;
            }
            
            .menu-toggle {
                display: block;
            }
            
            .page-title {
                font-size: 2rem;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .glass-card {
                padding: 1.5rem;
            }
            
            .feature-grid {
                grid-template-columns: 1fr;
            }
        }
        
        .hidden {
            display: none;
        }
        
        .progress-container {
            width: 100%;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            margin: 1rem 0;
            overflow: hidden;
        }
        
        .progress-bar {
            height: 8px;
            background: var(--gradient-primary);
            border-radius: 10px;
            transition: width 0.3s ease;
            width: 0%;
        }
    </style>
</head>
<body>
    <!-- Animated Background -->
    <div class="bg-animation" id="bgAnimation"></div>
    
    <!-- Sidebar -->
    <nav class="sidebar" id="sidebar">
        <div class="logo">
            <h1>SpectroSync</h1>
            <p>AI MUSIC ANALYSIS</p>
        </div>
        <ul class="nav-menu">
            <li class="nav-item">
                <div class="nav-link active" data-page="home">
                    <i class="fas fa-home"></i>
                    Home
                </div>
            </li>
            <li class="nav-item">
                <div class="nav-link" data-page="about">
                    <i class="fas fa-info-circle"></i>
                    About Project
                </div>
            </li>
            <li class="nav-item">
                <div class="nav-link" data-page="prediction">
                    <i class="fas fa-brain"></i>
                    Genre Classification
                </div>
            </li>
        </ul>
    </nav>
    
    <!-- Main Content -->
    <main class="main-content" id="mainContent">
        <header class="header">
            <button class="menu-toggle" id="menuToggle">
                <i class="fas fa-bars"></i>
            </button>
            <h1 class="page-title" id="pageTitle">Welcome</h1>
        </header>
        
        <!-- Home Page -->
        <div class="page active" id="home">
            <div class="hero-section">
                <div class="hero-content">
                    <h1 class="hero-title">SpectroSync</h1>
                    <p class="hero-subtitle">Next-Generation AI Music Genre Classification</p>
                    <div class="wave-container">
                        <div class="wave"></div>
                        <div class="wave"></div>
                        <div class="wave"></div>
                        <div class="wave"></div>
                        <div class="wave"></div>
                    </div>
                </div>
            </div>
            
            <div class="glass-card">
                <h2>🎵 Transform Your Music Experience</h2>
                <p>Our cutting-edge AI system analyzes audio tracks with precision, identifying music genres through advanced deep learning algorithms. Upload any audio file and discover the power of artificial intelligence in music analysis.</p>
            </div>
            
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-upload"></i>
                    </div>
                    <h3>Smart Upload</h3>
                    <p>Drag and drop or browse to upload your audio files. Supports MP3 format with intelligent preprocessing.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>AI Analysis</h3>
                    <p>Advanced neural networks process mel spectrograms to classify genres with high accuracy.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <h3>Lightning Fast</h3>
                    <p>Get results in seconds with our optimized prediction pipeline and efficient model architecture.</p>
                </div>
            </div>
        </div>
        
        <!-- About Page -->
        <div class="page" id="about">
            <div class="glass-card">
                <div class="about-content">
                    <h2>About SpectroSync</h2>
                    <p>Music genre classification has been a fascinating challenge in the intersection of artificial intelligence and audio processing. SpectroSync represents the next evolution in automated music analysis, leveraging state-of-the-art deep learning techniques to understand and categorize musical content.</p>
                    
                    <h3>🎯 Project Overview</h3>
                    <p>Our system utilizes convolutional neural networks trained on mel spectrogram representations of audio data. By converting audio signals into visual spectrograms, we can apply computer vision techniques to understand musical patterns and characteristics that define different genres.</p>
                    
                    <h3>📊 Dataset Information</h3>
                    <p>Built upon the renowned GTZAN dataset - the "MNIST of audio" - our model has been trained on a comprehensive collection of musical genres. Each audio sample undergoes sophisticated preprocessing including chunking, overlapping, and spectrogram generation.</p>
                    
                    <h3>🎼 Supported Genres</h3>
                    <div class="genre-list">
                        <span class="genre-tag">Blues</span>
                        <span class="genre-tag">Classical</span>
                        <span class="genre-tag">Country</span>
                        <span class="genre-tag">Disco</span>
                        <span class="genre-tag">Hip Hop</span>
                        <span class="genre-tag">Jazz</span>
                        <span class="genre-tag">Metal</span>
                        <span class="genre-tag">Pop</span>
                        <span class="genre-tag">Reggae</span>
                        <span class="genre-tag">Rock</span>
                    </div>
                    
                    <h3>⚡ Technology Stack</h3>
                    <p>Powered by TensorFlow and Keras for deep learning, LibROSA for audio processing, and advanced signal processing techniques. Our architecture employs multiple preprocessing stages including audio chunking with overlap, mel spectrogram computation, and dynamic resizing for optimal model input.</p>
                </div>
            </div>
        </div>
        
        <!-- Prediction Page -->
        <div class="page" id="prediction">
            <div class="glass-card">
                <h2>🎵 Genre Classification</h2>
                <p>Upload an audio file to discover its musical genre using our AI-powered classification system.</p>
                
                <div class="upload-area" id="uploadArea">
                    <div class="upload-icon">
                        <i class="fas fa-cloud-upload-alt"></i>
                    </div>
                    <h3>Drop your music file here</h3>
                    <p>or click to browse</p>
                    <input type="file" class="file-input" id="fileInput" accept=".mp3" />
                    <div style="margin-top: 1rem;">
                        <button class="btn btn-primary" id="browseBtn">
                            <i class="fas fa-folder-open"></i>
                            Choose File
                        </button>
                    </div>
                </div>
                
                <div id="fileInfo" class="hidden">
                    <div class="glass-card">
                        <h3>📁 File Information</h3>
                        <p id="fileName"></p>
                        <p id="fileSize"></p>
                    </div>
                </div>
                
                <div id="audioSection" class="hidden">
                    <div class="audio-player">
                        <div class="audio-visualizer">
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                            <div class="bar"></div>
                        </div>
                        <audio controls id="audioElement" style="width: 100%; margin-top: 1rem;">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    
                    <div style="text-align: center; margin-top: 2rem;">
                        <button class="btn btn-primary" id="predictBtn">
                            <i class="fas fa-magic"></i>
                            Analyze Genre
                        </button>
                    </div>
                </div>
                
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <h3>Analyzing your music...</h3>
                    <div class="progress-container">
                        <div class="progress-bar" id="progressBar"></div>
                    </div>
                    <p id="progressText">Initializing analysis...</p>
                </div>
                
                <div id="results" class="hidden">
                    <div class="result-card">
                        <h3>🎯 Classification Result</h3>
                        <div class="genre-result" id="genreResult"></div>
                        <p>Confidence: <span id="confidenceScore">95%</span></p>
                    </div>
                </div>
            </div>
        </div>
    </main>
    
    <script>
        // Global variables
        let selectedFile = null;
        let isAnalyzing = false;
        
        // Initialize particles
        function createParticles() {
            const container = document.getElementById('bgAnimation');
            const particleCount = 30;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 8 + 's';
                particle.style.animationDuration = (Math.random() * 4 + 6) + 's';
                container.appendChild(particle);
            }
        }
        
        // Navigation functionality
        function initNavigation() {
            const navLinks = document.querySelectorAll('.nav-link');
            const pages = document.querySelectorAll('.page');
            const pageTitle = document.getElementById('pageTitle');
            
            const titles = {
                'home': 'Welcome',
                'about': 'About Project',
                'prediction': 'Genre Classification'
            };
            
            navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Remove active class from all links
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    
                    // Hide all pages
                    pages.forEach(page => page.classList.remove('active'));
                    
                    // Show selected page
                    const pageId = link.getAttribute('data-page');
                    const targetPage = document.getElementById(pageId);
                    if (targetPage) {
                        targetPage.classList.add('active');
                        pageTitle.textContent = titles[pageId] || 'SpectroSync';
                    }
                });
            });
        }
        
        // Mobile menu functionality
        function initMobileMenu() {
            const menuToggle = document.getElementById('menuToggle');
            const sidebar = document.getElementById('sidebar');
            
            menuToggle.addEventListener('click', () => {
                sidebar.classList.toggle('active');
            });
            
            // Close sidebar when clicking outside on mobile
            document.addEventListener('click', (e) => {
                if (window.innerWidth <= 768 && 
                    !sidebar.contains(e.target) && 
                    !menuToggle.contains(e.target) && 
                    sidebar.classList.contains('active')) {
                    sidebar.classList.remove('active');
                }
            });
        }
        
        // File upload functionality
        function initFileUpload() {
            const uploadArea = document.getElementById('uploadArea');
            const fileInput = document.getElementById('fileInput');
            const browseBtn = document.getElementById('browseBtn');
            const fileInfo = document.getElementById('fileInfo');
            const audioSection = document.getElementById('audioSection');
            const audioElement = document.getElementById('audioElement');
            const fileName = document.getElementById('fileName');
            const fileSize = document.getElementById('fileSize');
            
            // Browse button click
            browseBtn.addEventListener('click', () => {
                fileInput.click();
            });
            
            // Upload area click
            uploadArea.addEventListener('click', (e) => {
                if (e.target === uploadArea || e.target.closest('.upload-icon') || e.target.tagName === 'H3' || e.target.tagName === 'P') {
                    fileInput.click();
                }
            });
            
            // Drag and drop
            uploadArea.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadArea.classList.add('dragover');
            });
            
            uploadArea.addEventListener('dragleave', (e) => {
                e.preventDefault();
                uploadArea.classList.remove('dragover');
            });
            
            uploadArea.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadArea.classList.remove('dragover');
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    handleFileSelection(files[0]);
                }
            });
            
            // File input change
            fileInput.addEventListener('change', (e) => {
                if (e.target.files.length > 0) {
                    handleFileSelection(e.target.files[0]);
                }
            });
            
            // Handle file selection
            function handleFileSelection(file) {
                // Validate file type
                if (!file.type.includes('audio/')) {
                    alert('Please select an audio file (MP3 format recommended).');
                    return;
                }
                
                // Validate file size (max 50MB)
                if (file.size > 50 * 1024 * 1024) {
                    alert('File size should be less than 50MB.');
                    return;
                }
                
                selectedFile = file;
                
                // Update file info
                fileName.textContent = `📄 ${file.name}`;
                fileSize.textContent = `📊 Size: ${(file.size / 1024 / 1024).toFixed(2)} MB`;
                
                // Show file info and audio section
                fileInfo.classList.remove('hidden');
                audioSection.classList.remove('hidden');
                
                // Setup audio player
                const url = URL.createObjectURL(file);
                audioElement.src = url;
                
                // Hide previous results
                document.getElementById('results').classList.add('hidden');
                
                // Add success effect
                uploadArea.style.borderColor = 'var(--accent-green)';
                uploadArea.style.backgroundColor = 'rgba(0, 255, 136, 0.1)';
                setTimeout(() => {
                    uploadArea.style.borderColor = 'var(--accent-green)';
                    uploadArea.style.backgroundColor = 'rgba(0, 255, 136, 0.05)';
                }, 1000);
            }
        }
        
        // Audio player functionality
        function initAudioPlayer() {
            const audioElement = document.getElementById('audioElement');
            const bars = document.querySelectorAll('.bar');
            
            audioElement.addEventListener('play', () => {
                bars.forEach(bar => {
                    bar.style.animationPlayState = 'running';
                });
            });
            
            audioElement.addEventListener('pause', () => {
                bars.forEach(bar => {
                    bar.style.animationPlayState = 'paused';
                });
            });
            
            audioElement.addEventListener('ended', () => {
                bars.forEach(bar => {
                    bar.style.animationPlayState = 'paused';
                });
            });
        }
        
        // Prediction functionality
        function initPrediction() {
            const predictBtn = document.getElementById('predictBtn');
            const loading = document.getElementById('loading');
            const results = document.getElementById('results');
            const genreResult = document.getElementById('genreResult');
            const confidenceScore = document.getElementById('confidenceScore');
            const progressBar = document.getElementById('progressBar');
            const progressText = document.getElementById('progressText');
            
            predictBtn.addEventListener('click', () => {
                if (!selectedFile || isAnalyzing) return;
                
                startAnalysis();
            });
            
            function startAnalysis() {
                isAnalyzing = true;
                predictBtn.disabled = true;
                
                // Show loading
                loading.classList.remove('hidden');
                results.classList.add('hidden');
                
                // Reset progress
                progressBar.style.width = '0%';
                progressText.textContent = 'Initializing analysis...';
                
                // Simulate analysis progress
                simulateProgress();
                
                // Simulate API call (replace with actual prediction logic)
                setTimeout(() => {
                    completeAnalysis();
                }, 4000);
            }
            
            function simulateProgress() {
                let progress = 0;
                const messages = [
                    'Loading audio file...',
                    'Extracting audio features...',
                    'Generating mel spectrograms...',
                    'Processing with neural network...',
                    'Analyzing patterns...',
                    'Finalizing classification...'
                ];
                
                const progressInterval = setInterval(() => {
                    progress += Math.random() * 15 + 5;
                    if (progress > 95) progress = 95;
                    
                    progressBar.style.width = progress + '%';
                    
                    const messageIndex = Math.floor((progress / 100) * messages.length);
                    if (messageIndex < messages.length) {
                        progressText.textContent = messages[messageIndex];
                    }
                    
                    if (progress >= 95) {
                        clearInterval(progressInterval);
                        progressBar.style.width = '100%';
                        progressText.textContent = 'Analysis complete!';
                    }
                }, 200);
            }
            
            function completeAnalysis() {
                // Hide loading
                loading.classList.add('hidden');
                
                // Mock prediction results
                const genres = ['Blues', 'Classical', 'Country', 'Disco', 'Hip Hop', 'Jazz', 'Metal', 'Pop', 'Reggae', 'Rock'];
                const randomGenre = genres[Math.floor(Math.random() * genres.length)];
                const confidence = Math.floor(Math.random() * 20 + 80);
                
                // Show results
                genreResult.textContent = randomGenre;
                confidenceScore.textContent = confidence + '%';
                results.classList.remove('hidden');
                
                // Add celebration effect
                createCelebrationEffect();
                
                // Reset state
                isAnalyzing = false;
                predictBtn.disabled = false;
            }
        }
        
        // Celebration effect
        function createCelebrationEffect() {
            const colors = ['#00ff88', '#00d4ff', '#ff6b6b', '#ffd93d'];
            const particleCount = 15;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.style.position = 'fixed';
                particle.style.width = '6px';
                particle.style.height = '6px';
                particle.style.background = colors[Math.floor(Math.random() * colors.length)];
                particle.style.borderRadius = '50%';
                particle.style.left = '50%';
                particle.style.top = '50%';
                particle.style.pointerEvents = 'none';
                particle.style.zIndex = '9999';
                
                document.body.appendChild(particle);
                
                const angle = (Math.PI * 2 * i) / particleCount;
                const velocity = 50 + Math.random() * 50;
                const tx = Math.cos(angle) * velocity;
                const ty = Math.sin(angle) * velocity;
                
                particle.animate([
                    { 
                        transform: 'translate(-50%, -50%) scale(0)', 
                        opacity: 1 
                    },
                    { 
                        transform: `translate(${tx - 50}%, ${ty - 50}%) scale(1)`, 
                        opacity: 0 
                    }
                ], {
                    duration: 1000,
                    easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
                }).onfinish = () => {
                    if (particle.parentNode) {
                        particle.parentNode.removeChild(particle);
                    }
                };
            }
        }
        
        // Responsive handling
        function handleResize() {
            const isMobile = window.innerWidth <= 768;
            const sidebar = document.getElementById('sidebar');
            
            if (!isMobile) {
                sidebar.classList.remove('active');
            }
        }
        
        // Keyboard shortcuts
        function initKeyboardShortcuts() {
            document.addEventListener('keydown', (e) => {
                if (e.ctrlKey || e.metaKey) {
                    switch(e.key) {
                        case '1':
                            e.preventDefault();
                            document.querySelector('[data-page="home"]').click();
                            break;
                        case '2':
                            e.preventDefault();
                            document.querySelector('[data-page="about"]').click();
                            break;
                        case '3':
                            e.preventDefault();
                            document.querySelector('[data-page="prediction"]').click();
                            break;
                    }
                }
                
                // Escape key to close mobile menu
                if (e.key === 'Escape') {
                    const sidebar = document.getElementById('sidebar');
                    if (sidebar.classList.contains('active')) {
                        sidebar.classList.remove('active');
                    }
                }
            });
        }
        
        // Initialize everything when DOM is loaded
        document.addEventListener('DOMContentLoaded', () => {
            createParticles();
            initNavigation();
            initMobileMenu();
            initFileUpload();
            initAudioPlayer();
            initPrediction();
            initKeyboardShortcuts();
            
            // Handle window resize
            window.addEventListener('resize', handleResize);
            handleResize();
            
            console.log('SpectroSync initialized successfully!');
        });
        
        // Error handling
        window.addEventListener('error', (e) => {
            console.error('SpectroSync Error:', e.error);
        });
        
        // Prevent default drag behaviors on the document
        document.addEventListener('dragover', (e) => e.preventDefault());
        document.addEventListener('drop', (e) => e.preventDefault());
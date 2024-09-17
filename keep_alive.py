from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Billu Mia - Your AI Discord Companion</title>
  <style>
    body {
      margin: 0;
      font-family: 'Arial', sans-serif;
      background: url('https://t4.ftcdn.net/jpg/01/97/06/89/360_F_197068986_KBwai9vz3MJ5naylkF4jNvSRJP0HzCOA.jpg') no-repeat center center fixed;
      background-size: cover;
      color: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }

    .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 80%;
      max-width: 1200px;
    }

    .glass-box {
      backdrop-filter: blur(1px);
      background: rgba(255, 255, 255, 0.1);
      border-radius: 15px;
      padding: 40px;
      text-align: center;
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      width: 45%;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .glass-box:hover {
      transform: translateY(-10px);
      box-shadow: 0 8px 40px rgba(0, 0, 0, 0.2);
    }

    .logo-circle {
      width: 150px;
      height: 150px;
      background-color: #7289DA;
      border-radius: 50%;
      margin: 0 auto;
      transition: transform 0.3s ease;
    }

    .logo-circle:hover {
      transform: rotate(360deg);
    }

    .name-image {
      margin: 20px 0;
    }

    .description {
      margin-top: 20px;
      font-size: 18px;
      color: #ccc;
    }

    .buttons {
      margin-top: 20px;
    }

    .buttons button {
      background: linear-gradient(45deg, #7289DA, #5865F2);
      border: none;
      color: white;
      padding: 15px;
      margin: 10px 0;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      width: 100%;
      text-align: center;
      transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }

    .buttons button:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .features {
      width: 45%;
      text-align: left;
    }

    .features h2 {
      font-size: 28px;
      background: linear-gradient(45deg, #7289DA, #5865F2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      transition: text-shadow 0.3s ease;
    }

    .features h2:hover {
      text-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .features ul {
      list-style-type: none;
      padding: 0;
      margin: 0;
    }

    .features ul li {
      margin: 10px 0;
      font-size: 18px;
      color: #ccc;
    }


    @media (max-width: 768px) {
      .container {
        flex-direction: column;
        align-items: center;
      }

      .features, .glass-box {
        width: 100%;
        margin: 20px 0;
      }

      .name-image img {
        width: 100%;
      }

      .buttons button {
        font-size: 14px;
        padding: 12px;
      }
    }

    @media (max-width: 480px) {
      .buttons button {
        font-size: 12px;
        padding: 10px;
      }
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="glass-box">
      <div class="logo-circle">
        <!-- Bot logo here -->
      </div>
      
      <div class="name-image">
        <img src="https://see.fontimg.com/api/rf5/zr0OG/ZTUwZTYwZTMyODlkNDZkODk1Yzg1MWYyMGQ2MzcyNjYub3Rm/QmlsbHUgTWlh/cat-paw.png?r=fs&h=77&w=1000&fg=1471F9&bg=FFFFFF&tb=1&s=77" alt="Billu Mia">
      </div>

      <p class="description">Hi! I am Billu. People call me Billu Mia. Your AI-Powered Discord Companion. You can chat with me whenever you want!</p>
      
      <div class="buttons">
        <button>🔗 Add to Discord</button>
        <button>📖 Learn More</button>
      </div>
    </div>

    <div class="features">
      <h2>What Billu Mia Can Do</h2>
      <ul>
        <li>🤖 Generate complex code in multiple languages</li>
        <li>💬 Real-time AI-powered conversations</li>
        <li>⚡ Seamless Discord integration for automation</li>
      </ul>
    </div>

  </div>
</body>
</html>
"
def run():
  app.run(host='0.0.0.0',port=8000)
def keep_alive():
  t = Thread(target=run)
  t.start()

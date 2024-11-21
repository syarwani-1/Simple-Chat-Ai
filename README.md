# 🌟 Groq AI Chat Companion 🤖

## Imperial-Themed Chat Application with Groq AI

### 🏰 Overview
Embark on a majestic conversational journey with this Python-powered AI chat application, leveraging the mighty Groq AI's powerful language model!

### 🛡️ Prerequisites
- Python 3.8+
- Groq API Key

### 🔧 Installation & Setup

#### For Standard Environments
```bash
# Clone the repository
git clone https://github.com/syarwani-1/Simple-Chat-Ai.git
cd Simple-Chat-Ai

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install python-dotenv groq
```

#### For Termux (Android)
```bash
# IMPORTANT: Install Rust first!
pkg install rust
pkg install python

# Then proceed with Python package installation
pip install python-dotenv groq
```

### 🗝️ API Key Configuration
1. Create a free account at [Groq Console](https://console.groq.com/)
2. Generate your API key
3. Create a `.env` file in your project root
4. Add your API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

### 🚀 Running the Chat Application
```bash
python chat_ai.py
```

### 🎮 Usage Options
- Type your messages normally
- Enter `exit`, `quit`, or `bye` to end the conversation

### 🛠️ Customization Options
- Adjust `temperature` for response creativity
- Modify `max_tokens` to control response length
- Change the AI model as needed

### 🌐 Supported Models
- `llama-3.1-70b-versatile` (default)
- Other Groq-supported models

### 🚧 Troubleshooting
- Ensure Python and pip are correctly installed
- Verify your API key's validity
- Check internet connectivity

### 🤝 Contributions
Imperial contributions and pull requests are most welcome!

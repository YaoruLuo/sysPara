# styles.py

def add_custom_styles():
    """添加自定义的CSS样式"""
    return """
    <style>
        body {
            background-color: #f4f7fc;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #009999;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 15px;
            margin: 10px 0;
            border: none;
        }
        .stButton>button:hover {
            background-color: #007777;
        }
        .stSelectbox>div>div>input {
            font-size: 16px;
        }
        h1 {
            color: #FF6F61;
            font-size: 36px;
            font-weight: 700;
        }
        h3 {
            color: #FF6F61;
            font-size: 10px;
            font-weight: 600;
        }
        .stMarkdown {
            font-size: 18px;
            color: #444;
        }
    </style>
    """

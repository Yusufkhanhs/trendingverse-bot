import os, requests, base64
from pytrends.request import TrendReq
import google.generativeai as genai

# Load Secrets from GitHub
WP_USER = os.getenv("WP_USER")
WP_APP_PW = os.getenv("WP_APP_PW")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def run_bot():
    # 1. Get Trend
    pytrends = TrendReq(hl='en-US')
    trend = pytrends.trending_searches(pn='united_states').iloc[0, 0]
    
    # 2. Generate Content
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Write a 800-word SEO news article about {trend}. Use H2 tags, no plagiarism, engaging for Google Discover. Output in HTML."
    content = model.generate_content(prompt).text

    # 3. Publish
    wp_url = "https://trendingverse.online/wp-json/wp/v2/posts"
    auth_header = base64.b64encode(f"{WP_USER}:{WP_APP_PW}".encode()).decode()
    headers = {'Authorization': f'Basic {auth_header}'}
    
    data = {'title': trend, 'content': content, 'status': 'publish'}
    res = requests.post(wp_url, headers=headers, json=data)
    print(f"Status: {res.status_code}")

if __name__ == "__main__":
    run_bot()

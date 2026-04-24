import os
import requests
import base64
import google.generativeai as genai
import xml.etree.ElementTree as ET

# Load Secrets
WP_USER = os.getenv("WP_USER")
WP_APP_PW = os.getenv("WP_APP_PW")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def get_trending_topic():
    # Fetching from Google News RSS instead of pytrends for 100% reliability
    url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    # Get the title of the very first trending news item
    first_item = root.find('.//item/title').text
    return first_item

def run_bot():
    try:
        topic = get_trending_topic()
        print(f"Targeting Topic: {topic}")

        # 1. Generate Article
        genai.configure(api_key=GEMINI_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Write a professional, SEO-friendly news article about: {topic}. Use HTML tags (H2, H3), ensure it's plagiarism-free, and optimized for Google Discover. Website: TrendingVerse.online"
        
        article_content = model.generate_content(prompt).text

        # 2. WordPress API Setup
        wp_url = "https://trendingverse.online/wp-json/wp/v2/posts"
        auth_string = f"{WP_USER}:{WP_APP_PW}"
        token = base64.b64encode(auth_string.encode()).decode()
        headers = {'Authorization': f'Basic {token}'}

        # 3. Publish
# ... inside your run_bot() function ...

        payload = {
            'title': topic,
            'content': article_content,
            'status': 'publish',
            'format': 'standard',
            'author': 1, # Usually 1 is the admin ID. Check your ID in 'Users' if needed.
        }

        res = requests.post(wp_url, headers=headers, json=payload)
        
        if res.status_code == 201:
            print("Successfully published to TrendingVerse!")
        else:
            print(f"Failed to publish. Status: {res.status_code}, Error: {res.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_bot()

# utils/ai_reporter.py
import os
import requests

def generate_bug_report(error_message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    # পিসির এনভায়রনমেন্ট বা সিস্টেম থেকে সিক্রেট কি পড়ে নেবে
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system", 
                "content": "You are an expert SQA Engineer. Create a highly professional, Jira-style bug report based on the provided test failure. Include: Bug Title, Severity, Environment, Steps to Reproduce, Expected Result, and Actual Result. Keep it concise and professional."
            },
            {
                "role": "user", 
                "content": f"My automated UI test failed with this error: {error_message}"
            }
        ]
    }
    
    print("\n[AI] AI is generating a professional bug report... Please wait...\n")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        
        if 'error' in response_data:
            print(f"❌ API Error Detected: {response_data['error']}")
            return

        report = response_data['choices'][0]['message']['content']
        
        with open("AI_Bug_Report.txt", "w", encoding="utf-8") as file:
            file.write(report)
            
        print("✅ Success! Professional Bug Report generated and saved as 'AI_Bug_Report.txt'")
        print("-" * 50)
        print(report)
        print("-" * 50)
        
    except Exception as e:
        print(f"Failed to generate AI report. Error: {e}")

if __name__ == "__main__":
    demo_error = "System accepted a past date (01/01/2020) for booking an appointment. URL redirected to #summary instead of showing an error."
    generate_bug_report(demo_error)
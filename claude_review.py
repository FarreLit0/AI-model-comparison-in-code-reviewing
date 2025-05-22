import requests
import time
import psutil
import json
import os

API_KEY = ""

code_path = "dataset/cpp/bug/const.cpp"
snippet_id = "const"
output_path = f"claude_outputs/cpp/bug/{snippet_id}.json"

# Read code
with open(code_path, "r", encoding="utf-8") as f:
    code = f.read()

prompt = (
    "Analyze the following javascript code and identify all issues.\n\n"
    "Group them into two categories:\n"
    "1. Bugs – Any logic errors, functional mistakes, incorrect behavior, or general programming bugs.\n"
    "2. Code quality issues – Bad practices, poor naming, redundancy, or maintainability problems.\n\n"
    "For each issue, list:\n"
    "- Category: BUG or QUALITY\n"
    "- Numbered format (1., 2., ...)\n"
    "- Explanation:\n"
    "  - What the issue is\n"
    "  - Why it’s a problem\n"
    "  - How to fix it\n\n"
    "If there are no bugs or quality issues, clearly state that.\n\n"
    "At the end, write exactly:\n"
    "Total bugs: <number>\n"
    "Total quality issues: <number>\n\n"
    "Do not restate the original code or use markdown formatting.\n\n"
    f"{code}"
)

headers = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

payload = {
    "model": "claude-3-opus-20240229",
    "max_tokens": 1024,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

start = time.perf_counter()
mem_before = psutil.Process().memory_info().rss

response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)

mem_after = psutil.Process().memory_info().rss
end = time.perf_counter()

result = {
    "id": snippet_id,
    "response": response.json()["content"][0]["text"],
    "response_time_sec": round(end - start, 2),
    "memory_used_bytes": mem_after - mem_before
}

os.makedirs("claude_outputs", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print(f"Claude reviewed {snippet_id} in {result['response_time_sec']}s")

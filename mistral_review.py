from together import Together
import time
import psutil
import json
import os

# API Key
client = Together(api_key="")

# Setup paths
code_path = "dataset/python/code_quality/next_permutation.py"
snippet_id = "next_permutation"
output_path = f"mistral_outputs/python/code_quality/{snippet_id}.json"

# Read code
with open(code_path, "r", encoding="utf-8") as f:
    code = f.read()

#Prompt for structured issue detection
prompt = (
    "Analyze the following python code and identify all issues.\n\n"
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

# Run inference
start = time.perf_counter()
mem_before = psutil.Process().memory_info().rss

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=1024,
    temperature=0.7,
    top_p=0.9
)

mem_after = psutil.Process().memory_info().rss
end = time.perf_counter()

# Extract result
model_reply = response.choices[0].message.content.strip()

result = {
    "id": snippet_id,
    "response": model_reply,
    "response_time_sec": round(end - start, 2),
    "memory_used_bytes": mem_after - mem_before
}

os.makedirs("mistral_outputs", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print(f"Mistral reviewed {snippet_id} in {result['response_time_sec']}s")

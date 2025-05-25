import openai
import time
import psutil
import os
import json

#Your OpenAI API Key
openai.api_key = ""

#Configuration
snippet_id = "next_permutation"
code_path = "dataset/python/code_quality/next_permutation.py"
output_path = f"openai_outputs/python/code_quality/{snippet_id}.json"

#Load code from file
with open(code_path, 'r', encoding='utf-8') as f:
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

#Time and memory tracking
start = time.perf_counter()
process = psutil.Process()
mem_before = process.memory_info().rss

#API call
response = openai.chat.completions.create(
    model="gpt-4o",
    max_tokens= 1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

mem_after = process.memory_info().rss
end = time.perf_counter()

#Save result
result = {
    "id": snippet_id,
    "response": response.choices[0].message.content,
    "response_time_sec": round(end - start, 2),
    "memory_used_bytes": mem_after - mem_before
}

os.makedirs("codex_outputs", exist_ok=True)
with open(output_path, "w", encoding='utf-8') as f:
    json.dump(result, f, indent=2)

print(f"Reviewed {snippet_id} in {result['response_time_sec']}s")
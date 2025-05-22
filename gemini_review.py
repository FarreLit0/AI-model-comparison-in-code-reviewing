from google import genai
import time
import psutil
import json
import os

# API key from Google AI Studio
client = genai.Client(api_key="")

# File and output setup
code_path = "dataset/cpp/bug/fun.cpp"
snippet_id = "fun"
output_path = f"gemini_outputs/cpp/bug/{snippet_id}.json"

# Load code
with open(code_path, "r", encoding="utf-8") as f:
    code = f.read()

# Prompt
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

# Timing + memory tracking
start = time.perf_counter()
mem_before = psutil.Process().memory_info().rss

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=prompt
)

mem_after = psutil.Process().memory_info().rss
end = time.perf_counter()

# Prepare result
result = {
    "id": snippet_id,
    "response": response.text.strip(),
    "response_time_sec": round(end - start, 2),
    "memory_used_bytes": mem_after - mem_before
}

os.makedirs("gemini_outputs", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Gemini reviewed {snippet_id} in {result['response_time_sec']}s")

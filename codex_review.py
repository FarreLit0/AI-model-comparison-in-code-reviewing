import openai
import time
import psutil
import os
import json

#Your OpenAI API Key
openai.api_key = ""  # Use your actual API key here

#Configuration
snippet_id = "naming_and_magic"
code_path = "dataset/python/naming_and_magic.py"
output_path = f"codex_outputs/python/{snippet_id}.json"

#Load code from file
with open(code_path, 'r', encoding='utf-8') as f:
    code = f.read()

#Prompt for structured issue detection
prompt = (
    "Analyze the following Python code and identify:\n"
    "Any logic or functional bugs (e.g. wrong comparisons, missing base cases, infinite loops).\n"
    "Any code quality issues (e.g. poor naming, deep nesting, magic numbers, bad style, unused variables, etc.).\n\n"
    "For each issue:\n"
    "- Number it (1., 2., 3., ...)\n"
    "- Explain:\n"
    "What the issue is\n"
    "Why it's a problem\n"
    "How to fix it\n\n"
    "If there are no bugs or issues, clearly state that.\n\n"
    "At the end, write exactly:\n"
    "Total bugs: <number>\n"
    "Total quality issues: <number>\n\n"
    "Do not include the original code again, and do not use markdown formatting.\n\n"
    f"{code}"
)

#Time and memory tracking
start = time.perf_counter()
process = psutil.Process()
mem_before = process.memory_info().rss

#API call
response = openai.chat.completions.create(
    model="gpt-4o",
    max_tokens= 512,
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
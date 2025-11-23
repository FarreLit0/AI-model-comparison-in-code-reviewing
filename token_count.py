import sys, argparse, re

def count_tokens_approx(text: str) -> int:
    
    byte_length = len(text.encode("utf-8"))
    return max(1, (byte_length + 3) // 4)

def main():
    parser = argparse.ArgumentParser(description="Estimate token count for any LLM response.")
    parser.add_argument("--file", help="Optional: path to a text file containing the response.")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            response = f.read()
    else:
        print("Paste your response below.")
        response = sys.stdin.read()

    token_est = count_tokens_approx(response)
    word_count = len(re.findall(r'\w+', response))
    bytes_len = len(response.encode('utf-8'))

    print("=== Token Estimation ===")
    print(f"Approx. tokens : {token_est}")
    print(f"Word count     : {word_count}")
    print(f"UTF-8 bytes    : {bytes_len}")

if __name__ == "__main__":
    main()

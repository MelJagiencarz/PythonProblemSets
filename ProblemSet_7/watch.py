import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    RE = re.search(r'<iframe[^>]*\s+src="([^"]+)"></iframe>', s)
    if RE:
        src = RE.group(1)
        src_match = re.match(r"^https?://(www\.)?youtube.com/embed/([\w-]+)$", src)
        if src_match:
            return f"https://youtu.be/{src_match.group(2)}"
        return None
    return None


if __name__ == "__main__":
    main()

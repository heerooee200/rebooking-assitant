"""Try the assistant: python ask.py "Can the passenger fly tomorrow for free?" UA100"""

import sys

from assistant.graph import ask

result = ask(sys.argv[1], sys.argv[2])
print("answer: ", result.get("answer"))
print("sources:", result.get("sources", []))

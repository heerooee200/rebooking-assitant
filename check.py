"""Runs the three task checks and prints one line per task: docker compose run --rm check"""

import hashlib
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).parent
TASKS = [("T1", "tests.test_task1_retries", "booking system down: gives up after 3 tries"),
         ("T2", "tests.test_task2_sources", "the answer lists its sources"),
         ("T3", "tests.test_task3_recall", "recall_at_k and the better retriever")]

for label, module, title in TASKS:
    suite = unittest.defaultTestLoader.loadTestsFromName(module)
    result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    problems = result.errors + result.failures
    if not problems:
        print(f"{label} ✓ {title}")
    else:
        lines = [l for l in problems[0][1].strip().splitlines() if l.strip() and not l.startswith("For troubleshooting")]
        last = lines[-1]
        print(f"{label} ✗ {title}: {last[:160].strip(' :')}")

files = [HERE / "check.py"] + sorted((HERE / "tests").glob("*.py"))
digest = hashlib.sha256(b"".join(f.read_bytes() for f in files)).hexdigest()[:8]
print(f"tests and check: {digest}")

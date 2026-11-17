"""Measures both retrievers on the evaluation questions: python evaluate.py"""

from assistant.data import EVAL, PASSAGES
from assistant.retrieval import RETRIEVERS, recall_at_k

relevant = [e["relevant"] for e in EVAL]
for name, retrieve in RETRIEVERS.items():
    ranked = [[p["id"] for p in retrieve(e["question"], PASSAGES, 3)] for e in EVAL]
    print(f"{name}: recall@3 = {recall_at_k(ranked, relevant, 3):.2f}")

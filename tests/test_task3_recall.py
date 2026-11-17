import random
import unittest

from assistant.data import EVAL, PASSAGES
from assistant.retrieval import CHOSEN_RETRIEVER, RETRIEVERS, recall_at_k


def reference(ranked, relevant, k):
    return sum(r in ids[:k] for ids, r in zip(ranked, relevant)) / len(relevant)


class Task3(unittest.TestCase):
    def test_recall_at_k_on_fresh_data(self):
        rng = random.Random()
        ids = [f"D{i}" for i in range(12)]
        for _ in range(200):
            n = rng.randint(1, 9)
            ranked = [rng.sample(ids, rng.randint(1, 8)) for _ in range(n)]
            relevant = [rng.choice(ids) for _ in range(n)]
            k = rng.randint(1, 6)
            self.assertAlmostEqual(recall_at_k(ranked, relevant, k), reference(ranked, relevant, k),
                                   msg=f"ranked={ranked} relevant={relevant} k={k}")

    def test_chosen_retriever_is_the_better_one(self):
        relevant = [e["relevant"] for e in EVAL]
        score = {name: reference([[p["id"] for p in r(e["question"], PASSAGES, 3)] for e in EVAL], relevant, 3)
                 for name, r in RETRIEVERS.items()}
        self.assertEqual(CHOSEN_RETRIEVER, max(score, key=score.get), f"recall@3: {score}")

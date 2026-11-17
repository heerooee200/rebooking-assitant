import unittest

from assistant.data import EVAL, PASSAGES
from assistant.graph import ask
from assistant.retrieval import CHOSEN_RETRIEVER, RETRIEVERS


class Task2(unittest.TestCase):
    def test_answer_lists_the_passages_it_used(self):
        for e in EVAL:
            expected = [p["id"] for p in RETRIEVERS[CHOSEN_RETRIEVER](e["question"], PASSAGES, 3)]
            result = ask(e["question"], "UA100")
            self.assertEqual(result.get("sources"), expected, e["question"])
            self.assertTrue(result["answer"])

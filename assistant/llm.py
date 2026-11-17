"""A fake, deterministic LLM so the exercise runs without API keys. It writes the answer from what it is given."""


def write_answer(question, passages, seats):
    rule = f"{passages[0]['title']}: {passages[0]['text']}" if passages else "No rule found."
    if seats is None:
        return f"{rule} I could not check seats right now."
    return f"{rule} Free seats on that flight: {seats}."

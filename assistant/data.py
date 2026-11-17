"""Fare-rule passages the assistant searches, and evaluation questions with the passage that answers each one."""

PASSAGES = [
    {"id": "FR-01", "title": "Same-day flight change",
     "text": "Passengers may move to an earlier or later flight on the same day for a fee of 75 dollars, if seats are available."},
    {"id": "FR-02", "title": "Change to another day",
     "text": "Moving to a flight on another day costs the fare difference. Basic Economy tickets cannot be changed."},
    {"id": "FR-03", "title": "Delays and cancellations",
     "text": "When our flight is delayed more than 3 hours or cancelled, the passenger can move to the next available flight for free, on any day."},
    {"id": "FR-04", "title": "Checked bags",
     "text": "The first checked bag costs 35 dollars. Premium members check two bags for free."},
    {"id": "FR-05", "title": "Missed connections",
     "text": "If a passenger misses a connection because the first flight was late, rebooking on the next flight is free and a meal voucher is given."},
    {"id": "FR-06", "title": "Upgrades",
     "text": "Upgrades to first class can be bought at the gate when seats are available. Miles cannot pay for upgrades within one hour of departure."},
    {"id": "FR-07", "title": "Pets in the cabin",
     "text": "Small dogs and cats may travel in the cabin in a carrier under the seat, for 125 dollars each way."},
    {"id": "FR-08", "title": "Refunds",
     "text": "Refundable tickets get their money back to the original card. Non-refundable tickets get travel credit valid for one year."},
]

EVAL = [
    {"question": "The flight is cancelled. Can the passenger fly tomorrow for free?", "relevant": "FR-03"},
    {"question": "How much is a dog in the cabin?", "relevant": "FR-07"},
    {"question": "Can a Basic Economy ticket move to next week?", "relevant": "FR-02"},
    {"question": "The first flight was late and she missed the connection. What do we offer?", "relevant": "FR-05"},
    {"question": "Can he pay for first class with miles 30 minutes before departure?", "relevant": "FR-06"},
    {"question": "Does a premium member pay for two bags?", "relevant": "FR-04"},
    {"question": "Where does the money go for a refundable ticket?", "relevant": "FR-08"},
    {"question": "Can the passenger take an earlier flight today, and what is the fee?", "relevant": "FR-01"},
    {"question": "Our flight is delayed 4 hours. Is moving to the next flight free?", "relevant": "FR-03"},
    {"question": "Is there a meal voucher after a missed connection?", "relevant": "FR-05"},
]

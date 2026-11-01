# Contribution added in branch GIT-EXAM (Task 6)
# Simple AI-style helper: sentiment check using keywords
POSITIVE = ["good", "great", "excellent", "happy", "love"]
NEGATIVE = ["bad", "poor", "sad", "hate", "terrible"]

text = input("Enter a sentence: ").lower()
score = sum(w in text for w in POSITIVE) - sum(w in text for w in NEGATIVE)
if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")

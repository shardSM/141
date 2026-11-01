# Simple keyword-based spam checker (added in branch GIT-EXAM)
SPAM_WORDS = ["free", "winner", "prize", "urgent", "click here", "lottery"]

def is_spam(text):
    text = text.lower()
    hits = [w for w in SPAM_WORDS if w in text]
    return len(hits) >= 2, hits

msg = input("Enter email text: ")
spam, words = is_spam(msg)
print("SPAM" if spam else "NOT SPAM", "| matched words:", words)

"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "I am excited",
    "I am Happy",
    "I really want to sleep so bad",
    "Today was a good day",
    "I hate writing",
    "This party is lit but I'm kinda stressed about tomorrow, feeling awesome yet totally exhausted",
    "Yo, this food is fire and delicious, but the service was trash and slow",
    "I'm so hyped for the game, it's gonna be epic and fun, but I'm lowkey nervous and scared",
    "Oh wow, I absolutely love getting stuck in traffic again 😩",
    "This is just fantastic, everything is going perfectly 🙄",
    
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive"   # "I am excited"
    "positive"   # "I am happy"
    "neutral"   # "I really want to sleep so bad"
    "positive"  # "Today was a good day"
    "negative"  # "I hate writing"
    "mixed",    # "This party is lit but I'm kinda stressed about tomorrow, feeling awesome yet totally exhausted"
    "mixed",    # "Yo, this food is fire and delicious, but the service was trash and slow"
    "mixed",    # "I'm so hyped for the game, it's gonna be epic and fun, but I'm lowkey nervous and scared"
    "negative", # "Oh wow, I absolutely love getting stuck in traffic again 😩"
    "negative", # "This is just fantastic, everything is going perfectly 🙄"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)

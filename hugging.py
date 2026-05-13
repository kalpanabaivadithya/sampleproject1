# ============================================================
# HUGGING FACE TRANSFORMERS - PIPELINE DEMOS
# The `pipeline()` function is a high-level API that lets you
# use pre-trained models with just one line of code.
# ============================================================

from transformers import pipeline  # Import the pipeline utility from HuggingFace


# ─────────────────────────────────────────────
# 1. SENTIMENT ANALYSIS
# Detects whether the given text is POSITIVE or NEGATIVE
# Default model: distilbert-base-uncased-finetuned-sst-2-english
# ─────────────────────────────────────────────
sentiment = pipeline("sentiment-analysis")
print("1. Sentiment Analysis:")
print(sentiment("I love learning AI"))
# Output: [{'label': 'POSITIVE', 'score': 0.99...}]


# ─────────────────────────────────────────────
# 2. TEXT GENERATION
# Given a starting prompt, the model continues/completes the text
# Default model: gpt2
# max_length=30 means the output won't exceed 30 tokens
# ─────────────────────────────────────────────
generator = pipeline("text-generation")
print("\n2. Text Generation:")
print(generator("Artificial Intelligence is", max_length=30))
# Output: [{'generated_text': 'Artificial Intelligence is ...'}]


# ─────────────────────────────────────────────
# 3. NAMED ENTITY RECOGNITION (NER)
# Identifies and classifies named entities like:
#   PERSON, ORGANIZATION, LOCATION, DATE, etc.
# grouped_entities=True merges tokens of the same entity together
# ─────────────────────────────────────────────
ner = pipeline("ner", grouped_entities=True)
print("\n3. Named Entity Recognition:")
print(ner("Elon Musk founded Tesla in America"))
# Output: [{'entity_group': 'PER', 'word': 'Elon Musk'}, ...]


# ─────────────────────────────────────────────
# 4. QUESTION ANSWERING
# Extracts the answer to a question FROM a given context paragraph
# It does NOT generate new answers — it finds them in the context
# ─────────────────────────────────────────────
qa = pipeline("question-answering")
print("\n4. Question Answering:")
print(qa(
    question="Who founded Tesla?",         # The question to answer
    context="Elon Musk founded Tesla company."  # Passage to search in
))
# Output: {'answer': 'Elon Musk', 'score': 0.99..., 'start': 0, 'end': 9}


# ─────────────────────────────────────────────
# 5. SUMMARIZATION
# Condenses a long piece of text into a shorter summary
# max_length / min_length control the summary length in tokens
# ─────────────────────────────────────────────
summarizer = pipeline("summarization")
print("\n5. Summarization:")
print(summarizer(
    "Artificial intelligence is transforming industries worldwide.",
    max_length=30,   # Summary won't be longer than 30 tokens
    min_length=10    # Summary won't be shorter than 10 tokens
))
# Output: [{'summary_text': '...'}]


# ─────────────────────────────────────────────
# 6. TRANSLATION (English → French)
# Translates text from one language to another
# Task name format: "translation_XX_to_YY"
# Default model: Helsinki-NLP/opus-mt-en-fr
# ─────────────────────────────────────────────
translator = pipeline("translation_en_to_fr")
print("\n6. Translation:")
print(translator("Hello, how are you?"))
# Output: [{'translation_text': 'Bonjour, comment allez-vous?'}]


# ─────────────────────────────────────────────
# 7. FILL MASK
# Predicts the missing word in a sentence
# The token [MASK] is the placeholder for the missing word
# Default model: bert-base-uncased (uses [MASK])
# ─────────────────────────────────────────────
fill_mask = pipeline("fill-mask")
print("\n7. Fill Mask:")
print(fill_mask("Machine learning is [MASK]."))
# Output: [{'sequence': 'Machine learning is important.', 'score': ...}, ...]


# ─────────────────────────────────────────────
# 8. TEXT CLASSIFICATION
# Assigns a label/category to a given text
# Similar to sentiment analysis but can support custom categories
# ─────────────────────────────────────────────
classifier = pipeline("text-classification")
print("\n8. Text Classification:")
print(classifier("This movie is amazing"))
# Output: [{'label': 'POSITIVE', 'score': 0.99...}]


# ─────────────────────────────────────────────
# 9. ZERO-SHOT CLASSIFICATION
# Classifies text into categories WITHOUT being trained on those labels
# You provide the candidate labels yourself at runtime
# ─────────────────────────────────────────────
zero_shot = pipeline("zero-shot-classification")
print("\n9. Zero Shot Classification:")
print(zero_shot(
    "I want to learn programming",
    candidate_labels=["education", "sports", "technology"]  # Custom labels
))
# Output: {'labels': ['technology', 'education', 'sports'], 'scores': [...]}


# ─────────────────────────────────────────────
# 10. FEATURE EXTRACTION
# Converts text into numerical vectors (embeddings)
# Useful for similarity comparison, clustering, search, etc.
# Output is a 3D array: [batch, tokens, hidden_size]
# ─────────────────────────────────────────────
feature = pipeline("feature-extraction")
print("\n10. Feature Extraction:")
print(feature("Hello world"))
# Output: [[[0.23, -0.11, ...], ...]]  ← numerical representation of text


# ─────────────────────────────────────────────
# 11. TEXT-TO-TEXT GENERATION
# A flexible model that takes text as input and generates text as output
# Can handle translation, summarization, Q&A, etc. in one model
# Default model: t5-base (trained on many NLP tasks)
# ─────────────────────────────────────────────
text2text = pipeline("text2text-generation")
print("\n11. Text2Text Generation:")
print(text2text("Translate English to German: How are you?"))
# Output: [{'generated_text': 'Wie geht es Ihnen?'}]


# ─────────────────────────────────────────────
# 12. TOKEN CLASSIFICATION
# Labels each individual token (word/subword) in a sentence
# Similar to NER but gives raw per-token labels (B-ORG, I-LOC, etc.)
# ─────────────────────────────────────────────
token_classifier = pipeline("token-classification")
print("\n12. Token Classification:")
print(token_classifier("Hugging Face is located in New York"))
# Output: [{'entity': 'I-ORG', 'word': 'Hugging'}, {'entity': 'I-LOC', 'word': 'New'}, ...]


# ─────────────────────────────────────────────
# BONUS: EXPLICIT MODEL SPECIFICATION
# Instead of using the default model, you can specify an exact model
# Here distilbert fine-tuned on SST-2 (movie review sentiment dataset)
# is explicitly loaded for text classification
# ─────────────────────────────────────────────
from transformers import pipeline
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"  # Explicit model name
)
print(classifier("Hello world"))
# Output: [{'label': 'POSITIVE', 'score': 0.99...}]
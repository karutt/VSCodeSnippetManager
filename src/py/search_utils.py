# search_utils.py
import difflib
import os


def calculate_similarity(key, query):
    key = key.lower()
    seq = difflib.SequenceMatcher(None, key, query)
    return seq.ratio()


def filter_and_rank_snippets(snippets, query):
    ranked_results = sorted(
        [(key, snippet, calculate_similarity(key, query)) for key, snippet in snippets.items()],
        key=lambda x: x[2],
        reverse=True,
    )
    return ranked_results[:20] if query else ranked_results


def filter_and_rank_languages(languages, query):
    ranked_results = sorted(
        [(key.split(".")[0], calculate_similarity(key.split(".")[0], query)) for key in languages],
        key=lambda x: x[1],
        reverse=True,
    )
    ranked_results = [key for key, _ in ranked_results]
    return ranked_results[:5] if query else ranked_results

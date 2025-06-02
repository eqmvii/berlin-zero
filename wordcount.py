#!/usr/bin/env python3
"""
Word count utility for the novel project.
Counts words in markdown files and provides statistics.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

def count_words(text):
    """Count words in text, ignoring markdown formatting."""
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r'`.*?`', '', text)
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Remove markdown links
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove markdown headers
    text = re.sub(r'^#+\s+.*$', '', text, flags=re.MULTILINE)
    # Count words
    words = re.findall(r'\b[\w\']+\b', text)
    return len(words)

def scan_directory(directory='.'):
    """Scan directory for markdown files and count words."""
    results = defaultdict(int)
    total_words = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    word_count = count_words(content)
                    results[rel_path] = word_count
                    total_words += word_count
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return results, total_words

def print_results(results, total_words):
    """Print word count results in a formatted table."""
    print("\n📚 NOVEL WORD COUNT STATISTICS 📚")
    print("=" * 60)
    print(f"{'FILE':<40} {'WORDS':>10}")
    print("-" * 60)
    
    # Sort by word count (descending)
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    for file_path, count in sorted_results:
        print(f"{file_path:<40} {count:>10,}")
    
    print("=" * 60)
    print(f"{'TOTAL WORD COUNT':<40} {total_words:>10,}")
    print(f"{'ESTIMATED PAGES (250 words/page)':<40} {total_words/250:>10,.1f}")
    print("=" * 60)

def main():
    """Main function to run the word count utility."""
    directory = '.'
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    
    print(f"Scanning directory: {directory}")
    results, total_words = scan_directory(directory)
    
    if not results:
        print("No markdown files found.")
        return
    
    print_results(results, total_words)

if __name__ == "__main__":
    main()

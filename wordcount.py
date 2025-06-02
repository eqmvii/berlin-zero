#!/usr/bin/env python3
"""
Word count utility for the novel project.
Counts words specifically in chapter_content.md files and provides statistics.
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

def scan_for_chapter_content(directory='.'):
    """Scan directory for chapter_content.md files and count words."""
    results = {}
    total_words = 0
    chapter_count = 0
    part_totals = defaultdict(int)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'chapter_content.md':
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                
                # Extract part and chapter information from the path
                path_parts = Path(rel_path).parts
                if len(path_parts) >= 2 and path_parts[0].startswith('part'):
                    part_name = path_parts[0]
                    chapter_name = path_parts[1] if len(path_parts) > 1 else 'unknown'
                    display_name = f"{part_name}/{chapter_name}"
                else:
                    display_name = rel_path
                    part_name = 'other'
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    word_count = count_words(content)
                    results[display_name] = word_count
                    total_words += word_count
                    part_totals[part_name] += word_count
                    chapter_count += 1
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return results, total_words, chapter_count, part_totals

def print_results(results, total_words, chapter_count, part_totals):
    """Print word count results in a formatted table."""
    print("\n📚 NOVEL CHAPTER WORD COUNT STATISTICS 📚")
    print("=" * 70)
    print(f"{'CHAPTER':<40} {'WORDS':>10} {'% OF NOVEL':>15}")
    print("-" * 70)
    
    # Sort by part and chapter number
    sorted_results = sorted(results.items())
    
    for chapter_path, count in sorted_results:
        percentage = (count / total_words * 100) if total_words > 0 else 0
        print(f"{chapter_path:<40} {count:>10,} {percentage:>14.1f}%")
    
    # Print part totals
    if part_totals:
        print("\n" + "-" * 70)
        print("PART SUMMARIES")
        print("-" * 70)
        for part_name, count in sorted(part_totals.items()):
            percentage = (count / total_words * 100) if total_words > 0 else 0
            print(f"{part_name:<40} {count:>10,} {percentage:>14.1f}%")
    
    # Print overall statistics
    print("=" * 70)
    print(f"{'TOTAL CHAPTERS':<40} {chapter_count:>10}")
    print(f"{'TOTAL WORD COUNT':<40} {total_words:>10,}")
    print(f"{'AVERAGE WORDS PER CHAPTER':<40} {(total_words/chapter_count if chapter_count else 0):>10,.1f}")
    print(f"{'ESTIMATED PAGES (250 words/page)':<40} {total_words/250:>10,.1f}")
    print("=" * 70)

def main():
    """Main function to run the word count utility."""
    directory = '.'
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    
    print(f"Scanning for chapter_content.md files in: {directory}")
    results, total_words, chapter_count, part_totals = scan_for_chapter_content(directory)
    
    if not results:
        print("No chapter_content.md files found.")
        return
    
    print_results(results, total_words, chapter_count, part_totals)

if __name__ == "__main__":
    main()

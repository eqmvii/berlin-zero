## Prompt 1

Add a readme markdown file. It should state that this project is about using windsurf to write a novel. It should be short.

Also create a prompts.md file and add this prompt to it. From here on out, each prompt should be added to that file.

## Prompt 2

Create a plot outline for the novel and save it in a new markdown file. 

This is a fantasy novel about a brown rabbit who grows up to become a knight. The main antagonist should be a space ship. There should be at least 10 characters including the rabbit's best friend, mom, and dad. There should be a subplot about learning new skills and lessons.

As before, save this prompt into prompts.md.

## Prompt 3

The novel will be 3 parts. Each part will be 15 chapters. 

Generate folders for part 1, part 2, and part 3. In each folder generate a folder for each of the 15 chapters.

## Prompt 4

Add the prior prompt, and this prompt, to prompts.md

Also update the chapter numbers - the chapters in part 2 should start at 16, and in part 3 should start at 31

## Prompt 5

Update chapter folder numbers. Part 1 should be 1-15, part 2 should be 16-30, and part 3 should be 31-45

Add this prompt to prompts.md as well

## Prompt 6

Please write summaries for each of the 3 parts and add them as a markdown file in the folder. Remember that the plot_outline.md has the overarching plot in it.

Add this prompt to prompts.md

## Prompt 7

Write the part 3 summary and add this and the prior prompt to prompts.md

## Prompt 8

Create a Dockerfile and docker-compose for this project. The dockerfile will be used to execute a python script to check wordcounts of files in this folder.

This needs to be containerized because I'm on a windows machine and don't want to install or run python. Instead, the dockerfile should have python3 installed, be able to see and run scripts in this repo (probably by volume mounts in the docker-compose), etc.

Model: Cascade (SWE-1)

## Prompt 9

Update the script so that when run, it counts the words for each and every chapter_content.md files located in any folder in this repository - rather than word ocunting arbitrary inputs.

Model: Cascade (SWE-1)

### Eric Note

That siad it was SWE-1, but it was actually claude 3.7 sonnet. It lies! 

## Prompt 10

Create part1/chapter2/chapter_content.md and write chapter 2. Use the chapter summary markdown file in that folder to guide you.

It must be at least 1,100 words long. Make it exciting!

Model: GPT-4.1 promo

## Prompt 11

Update the script so that it writes the output to a word_count.md markdown file in the root directory

Model: Cascade (SWE-1)

### Eric Note

That siad it was SWE-1, but it was acPrompt sent to claude 3.7 sonnet

Create part1/chapter1/chapter_content.md and write chapter 1. Use the chapter summary markdown file in that folder to guide you.

It must be at least 1,100 words long. Make it exciting!

Prompt sent to gemini 2.5 pro. It lies! 

## Prompt 11

Create part1/chapter1/chapter_content.md and write chapter 1. Use the chapter summary markdown file in that folder to guide you.

It must be at least 1,100 words long. Make it exciting!

Prompt sent to gemini 2.5 pro. It lies! 

## ERIC NOTE 

It's editing this file and jaming shit in random places!

# Prompt 12

Do it again for chatper 3

Model: GPT-4.1 promo

# Prompt 13

Write chapter 4

Model: GPT-4.1 promo

# Prompt 14

Write chapters 8, 9, 10, 11, 12, 13, 14, and 15.

Model: GPT-4.1 promo

# Part 2 summaries

SWE-1-lite

Open and read only the file part3\part3_summary.md - do not open or look at other files in the project.

After reviewing that file, produce one chapter_summary.md file in each of the 15 folders (chapter31 - chapter45) found in part3/.

Each of those 15 chapter_summary.md files should contain a short summary of the chapter of the novel - we will expand on them later. 

# Now write a chapter

Open and read only the file part2\chapter16\chapter_summary.md - do not open or look at other files in the project.

After reviewing that file, create a chapter_content.md file in part2\chapter16.

Write the full chapter for the story in that markdown file. It should be about 1,300 words. Make it exciting! 

# repeat for 3

Repeat exactly those steps in the following folders:

part2\chapter17
part2\chapter18
part2\chapter19

# Finally Working at sacle

SWE-1-lite

Repeat exactly those steps in the following 11 folders:

part2\chapter20

and each sequentially numbered folder through and including:

part2\chapter30

# Now we're cooking

Repeat exactly those steps in the following 11 folders:

part3\chapter31

and each sequentially numbered folder through and including:

part2\chapter38

# Last chapters!

Repeat exactly those steps in the following 11 folders:

part3\chapter39

and each sequentially numbered folder through and including:

part3\chapter45

# All the chapters were too short.

Open only the file part2/chapter17 and no other files in this project

It is a chapter in a novel, but it is short. Please expand it to be around 1,300 words.

# GPT did it then died in a fire 

Open only the file part2\chapter17\chapter_content.md and no other files in this project

It is a chapter in a novel, but it is short. Please expand it to be around 1,300 words.
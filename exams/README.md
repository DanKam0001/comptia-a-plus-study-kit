# Free practice exams

| Exam | Questions | Paper | Answer key |
|---|---|---|---|
| Core 1 (220-1201) | 84 | [Word](core1/practice-exam-1-questions.docx) · [Markdown](core1/practice-exam-1-questions.md) | [Word](core1/practice-exam-1-answers.docx) · [Markdown](core1/practice-exam-1-answers.md) |
| Core 2 (220-1202) | 90 | [Word](core2/practice-exam-1-questions.docx) · [Markdown](core2/practice-exam-1-questions.md) | [Word](core2/practice-exam-1-answers.docx) · [Markdown](core2/practice-exam-1-answers.md) |

## How to use them

1. **Take the paper under exam conditions:** 90 minutes, no notes, no lookups. Print the Word file or use the Markdown.
2. **Mark your answers, then open the answer key.** Each explanation says why the right answer is right and why the others are wrong.
3. **Use the objective and domain tag** on every miss to find the part of the series that covers it. A cluster of misses in one domain tells you more than your total.
4. **Don't retake the same paper straight away.** You'll remember answers, not the material. Drill the weak parts, then come back.

## What these are, and aren't

- Scenario-style multiple choice, with some choose-two questions, spread across the exam domains in roughly the published weights.
- **No hands-on tasks.** The real exam has performance-based questions (PBQs). For hands-on practice use the labs in each part's folder.
- **Not the real exam.** They don't contain real exam questions and aren't a prediction of what you'll see. CompTIA also uses scaled scoring, so the percentage guide in each answer key is only a rough indicator.
- **Coverage is deliberately uneven.** Each paper is one sample of the objectives, not all of them. For example, Core 2 has few Linux and macOS questions, and Core 1 has few on cable categories and wireless standards. Use CompTIA's objectives as your checklist, and use more than one source of practice questions.

## Quality note

Every question was reviewed against CompTIA's published objectives. In the Core 1 review, 6 questions were removed (out of scope or duplicates) and 9 corrected. In the Core 2 review, 6 were corrected. If you think a question or answer is wrong, please open an issue with the question number.

## Rebuilding the files

The source questions are in `src/core1.json` and `src/core2.json`. To rebuild the Word and Markdown files:

```
pip install python-docx
python tools/build_exams.py
```

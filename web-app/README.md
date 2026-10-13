# APPSC Group-1 2026–2027 Master Study Portal

A responsive, high-performance React application designed for APPSC Group-1 preparation (Notification No. 07/2026, Exam Date: 24/01/2027). Built with a distraction-free dark grey design system, high-contrast readable typography, and complete offline access to all 40 syllabus topics.

---

## Key Features

- **Dark Grey & High-Contrast Typography**:
  - Background palette (`#121316` / `#1a1b20` / `#22242c`) with crisp white headings (`#ffffff`) and readable light text (`#e2e4ea`).
  - Adjustable reading font scaling (`A-` / `100%` / `A+`).
  - Styled scrollbars and responsive data tables with horizontal scroll containers.

- **4 Core Study Modes**:
  1. **Notes Reader**: Read all 40 modular topics with hierarchical headings, comparative markdown tables, verified Wikimedia Commons diagrams/photographs with zoom lightbox, and inline PYQs.
  2. **MCQ Practice Bank (200 Questions)**: Interactive Screening Prelims quiz interface with clickable options, instant green/red feedback, score/accuracy counter, and detailed explanations.
  3. **Mains Question Bank (121 Questions)**: Comprehensive analytical questions repository across Paper-II to Paper-V, featuring expandable evaluator blueprints and model approaches.
  4. **Progress Dashboard**: Real-time syllabus coverage meter, subject-by-subject completion bars, bookmark drawer, and study statistics.

- **Search & Filter Navigation**:
  - Full-text search across all 40 topics, headings, and syllabus mappings.
  - Quick paper filters: All Papers, Paper II, Paper III, Paper IV, Paper V, and Screening Prelims.
  - Per-topic completion checklist and bookmarking (persisted in `localStorage`).
  - Print / PDF export support for individual topic notes.

---

## How to Run Locally

### Start Development Server
```bash
cd /Users/imandisaiganesh/Documents/appsc/web-app
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### Preview Production Build
```bash
cd /Users/imandisaiganesh/Documents/appsc/web-app
npm run preview
```
Open [http://localhost:4173](http://localhost:4173) in your browser.

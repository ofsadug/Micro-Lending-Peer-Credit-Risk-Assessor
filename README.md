# UE24CS341A: Software Engineering – Lab Submissions

**Name:** Apurv Kumar Singh  
**SRN:** PES1UG24CS077  
**Class:** 5B  
**Problem Statement #33:** Retail, E-Commerce & Finance – Micro-Lending & Peer Credit Risk Assessor

A peer-to-peer micro-finance platform that calculates borrower risk scores using heuristic rules, generates structured repayment schedules, and triggers automated default warnings.  
**Actors:** Borrower, Peer Lender

## Lab overview

| Lab | Topic | Folder |
| :-- | :-- | :-- |
| Lab 1 | Requirements Engineering & UML Use-Case Modelling | [`Lab1/`](Lab1/) |
| Lab 2 | Agile Backlog Creation & Sprint Simulation in Jira | [`Lab2/`](Lab2/) |
| Lab 3 | Component Modelling & Architectural Pattern Selection | [`Lab3/`](Lab3/) |
| Lab 4 | Vibe Coding – Fixing & Extending a 2048 Game with an LLM | [`Lab-4/`](Lab-4/) |
| Lab 5 | Static Code Analysis | [`Lab-5/`](Lab-5/) |
| Lab 6 | Code and Branch Coverage Analysis | [`Lab-6/`](Lab-6/) |
| Lab 7 | Fuzz Testing for Input Validation Bugs | [`Lab-7/`](Lab-7/) |

---

## Lab 1 – Requirements Engineering & UML Use-Case Modelling

- `Lab1_PES1UG24CS077_5B.pdf` – consolidated Lab 1 submission.
- `PES1UG24CS077_Requirements_Table.md` – exactly 5 functional requirements (FR-001 to FR-005) and 2 non-functional requirements (NFR-001, NFR-002), with ID, type, description, priority, acceptance criteria and rationale.
- `PES1UG24CS077_UML_UseCase_Diagram.png` – actors and primary use cases, including `include` and `extend` relationships.
- `PES1UG24CS077_UseCase_Flow_Specification.pdf` – use-case flow for “Compute Borrower Credit Risk Rating”, with preconditions, postconditions, main success scenario and an alternate flow.

## Lab 2 – Agile Backlog Creation & Sprint Simulation in Jira

- `Lab2_PES1UG24CS077_5B.pdf` – 3 epics, 8 user stories (30 story points), backlog, Sprint 1 and Sprint 2 boards, burndown charts and reflection answers.
- Jira workspace: [Micro-Lending & Peer Credit Risk Assessor – backlog](https://apurvkumar149.atlassian.net/jira/software/c/projects/MLPCRA/boards/36/backlog?epics=visible).

## Lab 3 – Component Modelling & Architectural Pattern Selection

- `PES1UG24CS077_Lab3_Submission.pdf` – combined submission (page 1: component diagram; page 2: architectural justification).
- `PES1UG24CS077_Lab3_Component_Diagram.png` / `.pdf` – UML component diagram showing a layered architecture with 5 components and 4 interfaces.
- `PES1UG24CS077_Lab3_Architectural_Justification.pdf` – justification covering the architecture choice, reasons, a security advantage and a performance benefit.

## Lab 4 – Vibe Coding (Scenario 14: 2048)

- Assigned repository: [SETAPESU26/14_2048](https://github.com/SETAPESU26/14_2048).
- `main.py`, `game.py`, `board.py` – implementation updates addressing the double-merge bug, score handling, win/no-move detection, input validation, one-level undo, best score and move feedback.
- `PES1UG24CS077_Lab4_Before.mp4` / `PES1UG24CS077_Lab4_After.mp4` – 10-second gameplay recordings before and after the changes.
- `PES1UG24CS077_Lab4_Chat_History.pdf` and `LLM_CHAT_LINK.md` – LLM interaction history and chat link.

## Lab 5 – Static Code Analysis

- [`music_catalog.py`](Lab-5/music_catalog.py) – updated music-catalog application.
- [`issues.md`](Lab-5/issues.md) – analysis of the identified issues, their types, locations and fixes.
- [`reports/before/`](Lab-5/reports/before/) and [`reports/after/`](Lab-5/reports/after/) – static-analysis reports before and after remediation.
- The fixes address SQL injection risk, unsafe pickle deserialization, mutable default arguments, broad exception handling, naming and documentation, readability and formatting.
- Recorded analysis results: Pylint improved from 4.57/10 to 10.00/10; Bandit findings went from 2 medium and 2 low to no findings; Flake8 findings went from 7 to no findings. See `issues.md` for the recorded details and verification note.

## Lab 6 – Code and Branch Coverage Analysis

- [`README.md`](Lab-6/README.md) – Lab 6 setup and reproduction instructions.
- [`parking_fee.py`](Lab-6/parking_fee.py) – parking-fee application under test, copied from the instructor-assigned repository.
- [`CodeCoverageTest_19_parking_fee.py`](Lab-6/CodeCoverageTest_19_parking_fee.py) – pytest cases for code/line coverage.
- [`BranchCoverageTest_19_parking_fee.py`](Lab-6/BranchCoverageTest_19_parking_fee.py) – pytest cases for branch coverage.
- `Code_Coverage_Terminal.png` and `Branch_Coverage_Terminal.png` – terminal execution evidence.
- Recorded results: 100% code coverage (34 statements, 0 missed) and 100% branch coverage (24 branches, 0 partial branches). The branch-coverage suite recorded 20 passing tests.

## Lab 7 – Fuzz Testing for Input Validation Bugs

- [`processor.py`](Lab-7/processor.py) – corrected parking utility application with input validation for all three functions.
- [`test_processor.py`](Lab-7/test_processor.py) – Hypothesis-based property/fuzz tests for `minutes_parked()`, `hourly_rate()` and `format_plate()`.
- The fuzz tests cover valid inputs, invalid time values and intervals, unsupported vehicle types, malformed number plates and incorrect input types.
- Recorded results: the original application produced 8 failing tests and 3 passing tests; after the fixes, all 11 tests passed.
- To reproduce the final test run, install the dependencies and run pytest from the `Lab-7/` directory:

  ```bash
  python -m pip install hypothesis pytest
  python -m pytest -vv test_processor.py
  ```

---

## Repository structure

```text
.
├── Lab1/
├── Lab2/
├── Lab3/
├── Lab-4/
├── Lab-5/
├── Lab-6/
├── Lab-7/
└── README.md
```

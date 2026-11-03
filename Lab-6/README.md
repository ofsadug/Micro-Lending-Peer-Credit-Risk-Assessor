# Lab 6 — Code and Branch Coverage Analysis

**Assigned application:** `parking_fee.py`, copied unchanged from the instructor-assigned repository `SETAPESU26/L6_L7_19_parking_fee`, in its `Lab 6` folder.

## Files

- `parking_fee.py` — application under test.
- `CodeCoverageTest_19_parking_fee.py` — independent pytest test file for code/line coverage.
- `BranchCoverageTest_19_parking_fee.py` — independent pytest test file for branch coverage.
- `Code_Coverage_Terminal.png` — terminal evidence for code coverage.
- `Branch_Coverage_Terminal.png` — terminal evidence for branch coverage.
- `Lab-6_Submission_Evidence.pdf` — combined coverage report and terminal screenshots.
- `GITHUB_PUSH_INSTRUCTIONS.md` — commands for publishing the folder with two separate commits.

## Install

```bash
python -m pip install pytest coverage
```

## Code coverage

```bash
coverage erase
coverage run --source=parking_fee -m pytest -q CodeCoverageTest_19_parking_fee.py
coverage report -m
```

Verified result: 16 tests passed; 34 statements, 0 missed; 100% code coverage.

## Branch coverage

```bash
coverage erase
coverage run --branch --source=parking_fee -m pytest -q BranchCoverageTest_19_parking_fee.py
coverage report -m
```

Verified result: 20 tests passed; 34 statements, 0 missed; 24 branches, 0 partial; 100% total coverage.

The `--source=parking_fee` option restricts the coverage measurement to the application module rather than counting test code. See `GITHUB_PUSH_INSTRUCTIONS.md` for the two required Git commits and push steps.

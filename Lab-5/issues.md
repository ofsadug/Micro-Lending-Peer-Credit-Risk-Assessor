# Lab 5: Static Code Analysis

Name: Apurv Kumar Singh  
SRN: PES1UG24CS077  
Assigned file: `music_catalog.py`

Line numbers refer to the original file in the assigned repository.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk — B608 | Security, Medium | 10 | Title and artist values were inserted directly into SQL using string formatting. | Used SQL placeholders and passed the values separately. |
| Unsafe pickle loading — B301 | Security, Medium | 33 | Loading an untrusted pickle can execute code. | Replaced pickle with JSON and checked that the playlist is a list of strings. |
| Pickle import — B403 | Security, Low | 1 | Bandit flagged the pickle module. | Removed the import and used JSON for saving and loading. |
| Standard random generator — B311 | Security-tool warning, Low | 17 | Bandit flags standard random functions as unsuitable for security-sensitive uses. | Used `secrets.choice` to clear the finding. A music shuffle itself does not require secure randomness. |
| Mutable default list — W0102 | Bug | 9 | Calls without a playlist shared the same default list. | Changed the default to `None` and created a new list inside the function. |
| Bare except — W0702, E722 | Error handling | 39 | The handler hid database errors. An empty SUM also returned None rather than zero. | Removed the bare handler and used SQL COALESCE for the empty-table case. |
| Naming and missing docstrings — C0103, C0114, C0116 | Code quality | 1, 9, 15, 20, 28, 32, 36, 43 | Functions used mixed-case names and lacked documentation. | Used snake_case names and added docstrings. |
| Redundant else — R1705 | Readability | 22–25 | The else was unnecessary after a return. | Removed the else and returned the result directly. |
| String formatting — C0209 | Code quality | 10 | Pylint flagged the old formatting style in the SQL statement. | Removed SQL string formatting entirely; an f-string would not fix the injection risk. |
| Ambiguous variable — E741 | Readability | 47 | The variable `l` was difficult to read. | Renamed it to `loaded_playlist`. |
| Multiple statements on one line — C0321, E701 | Formatting | 48 | The condition and print statement were on one line. | Moved the print to an indented line. |
| Long lines — C0301, E501 | Formatting | 6, 10, 21, 49 | Several lines exceeded the default line-length limits. | Wrapped the statements to meet the default limits. |

## Results

| Tool | Before | After |
|---|---|---|
| Pylint | 4.57/10 | 10.00/10 |
| Bandit | 2 medium and 2 low findings | No findings |
| Flake8 | 7 findings | No findings |

Reports are saved in `reports/before` and `reports/after`. The final Flake8
report is empty because there are no findings. No warnings were suppressed.
These reports were generated in the assisted preparation environment; rerun
locally to verify them on the submission machine.

The updated functions use snake_case names. Playlist data is now JSON bytes,
not pickle, so old pickle data is not supported. The main guard prevents the
demo from running on import. An empty catalog returns zero total plays and
None for a random selection.

---
name: Update Statuses
about: Request that the statuses be updated within ergast-py
title: "[ENHANCEMENT] Update finishing statuses"
labels: enhancement
assignees: ''

---

**Information**
The following statuses have been identified as missing from Ergast-py and therefore need adding:
{{ env.MISSING_STATUSES_FORMATTED }}

Please ensure you update the following files:
- `./ergast_py/constants/status_type.py`
- `./utils/status-action/current_statuses.json`

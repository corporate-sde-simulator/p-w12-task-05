# OPS-403: Build Multi-Service Health Check Endpoint

**Status:** In Progress · **Priority:** Medium
**Sprint:** Sprint 33 · **Story Points:** 5
**Reporter:** Platform Team · **Assignee:** You (Intern)
**Labels:** `observability`, `health`, `python`, `feature`
**Task Type:** Feature Ship

---

## Description

Build a health check system that checks database, cache, and external API dependencies.
Return overall status: healthy (all pass), degraded (some fail), unhealthy (all fail).

## Acceptance Criteria

- [ ] Checks 3 dependencies (db, cache, api)
- [ ] Returns overall status + individual results
- [ ] Includes response time for each check
- [ ] Handles timeouts gracefully
- [ ] All tests pass

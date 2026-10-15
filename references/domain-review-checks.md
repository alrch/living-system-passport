# Domain review checks

Use only checks relevant to the function and the project's accepted rules. These are investigation prompts, not a checklist that every project must satisfy.

- **Forms and tables:** Trace consequential values from visible input and defaults through client payload, API validation, transformation, storage, readback, and export. Check omitted values against explicit empty or false values. Compare displayed filters with list, count, and export queries.
- **Access and privacy:** Check both UI visibility and the callable server route. Inspect serialized responses and direct file or object URLs for data exposed beyond the intended role or audience. Verify transitions with allowed and denied actors.
- **State changes:** Follow ordered writes and side effects, including audit, messages, and integrations. Test a failure between steps, retry, idempotency, and competing decisions when relevant. A warning in the UI does not enforce a server rule.
- **Analytics and time:** Define each metric's event, population, numerator, denominator, window, exclusions, units, and displayed label. Trace the actual value to every display and export. Check date boundaries and time zones where they affect the rule.
- **Exports and files:** Define source rows and an allowed column set; check access scope, row limits, encoding, and spreadsheet formula injection where applicable. For files, distinguish list access from byte access, and inspect retention, deletion, and shared references.
- **External delivery:** Distinguish a local event or queue row from provider acceptance and recipient delivery. Check eligibility when sending, cancellation, retries, ambiguous results, and evidence of the actual external receipt.
- **Media and accessibility:** Compare the promised behavior with each supported media source and viewer. Verify the content endpoint as well as the listing page, and distinguish a transcript from timed captions where that matters.
- **Tests and evidence:** Confirm that mocks exercise the consequential schema and contract, that a test covers the current route, and that its dated result supports the exact acceptance claim. A scenario catalog entry is not execution evidence.

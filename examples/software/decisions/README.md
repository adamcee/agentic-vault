# Decisions

Architecture Decision Records (ADRs) and Product Decision Records (PDRs). Each records context, the decision, alternatives considered, and consequences.

New records are drafted in chat and written only after the owner approves ([[vault-guide/decision-propagation-protocol]]).

- [[decisions/_BASES_SCHEMA]]: frontmatter, status meanings, tag list, and search recipes.

## Technical

- [[decisions/technical/ADR-T001-react-native-manager-app|ADR-T001]]: one React Native app for managers and staff. Superseded by ADR-T002.
- [[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]]: one responsive web app with a PWA staff view and SMS alerts.
- [[decisions/technical/ADR-T003-django-and-postgresql|ADR-T003]]: Django on PostgreSQL, with PostgreSQL as the only datastore.

## Product

- [[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]]: $49 a month per location with unlimited staff.
- [[decisions/product/PDR-P002-manager-approval-for-swaps|PDR-P002]]: every shift swap needs manager approval. Weakened by pilot data on 2026-10-06.

## Rejected

- [[decisions/rejected/ADR-T004-shared-spreadsheet-backend|ADR-T004]]: a shared spreadsheet as the schedule backend.

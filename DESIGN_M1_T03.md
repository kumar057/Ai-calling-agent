# Design Note: Persistence Boundary (M1-T03)

## Objective
Establish a persistence boundary and local database setup using SQLite, ensuring future compatibility with Postgres (Decision D02). 

## Library Options Considered

1. **SQLAlchemy 2.x with Alembic**
   - *Pros:* Industry standard, excellent abstraction over SQLite and Postgres, strong typing support in 2.x, robust migration management (Alembic). Highly compatible with FastAPI.
   - *Cons:* Steeper learning curve, slightly verbose setup.

2. **SQLModel (with Alembic)**
   - *Pros:* Combines Pydantic and SQLAlchemy, less boilerplate, designed for FastAPI.
   - *Cons:* Still relatively new, sometimes harder to handle complex schema migrations compared to pure SQLAlchemy.

3. **Tortoise ORM**
   - *Pros:* Native async, simple syntax.
   - *Cons:* Smaller ecosystem, migrations via Aerich can be less robust than Alembic.

## Proposed Choice
**SQLAlchemy 2.x with Alembic** is proposed. It provides the most robust Postgres compatibility and migration path, ensuring no SQLite-specific SQL leaks into the codebase. 

## Implementation Details
- **Repository Pattern:** `LeadRepository` will expose methods like `save`, `get_by_id`, `get_by_phone`, and `list` (paginated).
- **Configuration:** DB location read from `DATABASE_URL` in `.env`. If missing, the app fails to start (no silent default).
- **Schema:** 
  - `id` (PK, integer or UUID)
  - `name` (string)
  - `phone_number` (string, indexed, unique handling depending on family sharing - currently just indexed for lookup)
  - `source` (string)
  - `contact_permission_granted` (boolean)
  - `course_interest` (string, nullable)
  - `is_suppressed` (boolean, default False)
  - `created_at` (datetime)
  - `updated_at` (datetime)

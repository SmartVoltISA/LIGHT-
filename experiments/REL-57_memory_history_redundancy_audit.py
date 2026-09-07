import numpy as np

# REL-57: test whether retained history can distinguish duplicated sectors.
# Base dynamics: x_{t+1}=A x_t. Two identical sectors are duplicated copies.
# If history is also duplicated identically, no new observable distinction exists.
# If an independent retained trace differs, it creates a genuine relation.

rng = np.random.default_rng(57)
A = np.array([[0.0, 1.0], [-1.0, 0.0]])

max_dup_state_error = 0.0
max_dup_history_error = 0.0
max_independent_trace_difference = 0.0

for _ in range(100):
    x = rng.normal(size=2)
    h = rng.normal(size=2)
    x2 = x.copy()
    h2 = h.copy()
    for _ in range(20):
        x = A @ x
        x2 = A @ x2
        h = A @ h
        h2 = A @ h2
    max_dup_state_error = max(max_dup_state_error, np.linalg.norm(x - x2))
    max_dup_history_error = max(max_dup_history_error, np.linalg.norm(h - h2))

# Independent memory is represented by a retained trace not generated from
# the same history. It therefore supplies a new relation/observable.
for _ in range(100):
    x = rng.normal(size=2)
    h1 = rng.normal(size=2)
    h2 = h1 + rng.normal(scale=0.5, size=2)
    max_independent_trace_difference = max(
        max_independent_trace_difference, np.linalg.norm(h1 - h2)
    )

print(f"max_duplicate_state_error={max_dup_state_error:.17g}")
print(f"max_duplicate_history_error={max_dup_history_error:.17g}")
print(f"max_independent_trace_difference={max_independent_trace_difference:.17g}")

assert max_dup_state_error < 1e-15
assert max_dup_history_error < 1e-15
assert max_independent_trace_difference > 1e-3

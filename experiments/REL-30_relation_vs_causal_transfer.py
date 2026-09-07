from math import ceil

N = 100
edge_length = 1.0
R = 2
tau = 0.5
D = N - 1
T_min = ceil(D / R) * tau
v_bound = D * edge_length / T_min

# Structural relation: part of initial graph state, not a transfer event.
structural_relation_exists_at_t0 = True

# Causal transfer: requires traversing the route in bounded local updates.
transfer_time_positive = T_min > 0
transfer_speed_finite = v_bound < float("inf")

assert structural_relation_exists_at_t0
assert transfer_time_positive
assert transfer_speed_finite
assert T_min == 25.0
assert abs(v_bound - 3.96) < 1e-12

print("REL-30 PASS")
print(f"nodes={N}")
print(f"distance_edges={D}")
print(f"R={R}")
print(f"tau={tau}")
print(f"minimum_transfer_time={T_min}")
print(f"transfer_speed_bound={v_bound}")
print("structural_relation_at_t0=True")
print("CONCLUSION: relation existence and causal transfer are distinct model objects.")

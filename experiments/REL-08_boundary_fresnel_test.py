# REL-08: normal-incidence Fresnel boundary test for ideal lossless media.
# r=(n1-n2)/(n1+n2), R=r^2, T=1-R for this normalized lossless case.

cases = [(1.0, 1.5), (1.0, 2.0), (1.5, 2.0), (1.0, 1.0)]

print('REL-08 Fresnel boundary checks')
for n1, n2 in cases:
    r = (n1 - n2) / (n1 + n2)
    R = r * r
    T = 1.0 - R
    print(f'n1={n1:g} n2={n2:g} r={r:.12g} R={R:.12g} T={T:.12g} R+T={R+T:.12g}')

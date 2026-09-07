# LIGHT — Gauge Structure

## Core fact
QED is a local U(1) gauge theory. Requiring local phase invariance of charged matter introduces a gauge field A_mu and the covariant derivative D_mu.

## Transformation
ψ(x) → exp(−i q α(x)) ψ(x)

A_mu(x) → A_mu(x) + ∂_mu α(x)

The observable physics is unchanged by this gauge redundancy.

## Connection interpretation
A_mu behaves mathematically like a connection: it tells the theory how to compare the phase of a charged field across spacetime while preserving local gauge covariance.

F_muν = ∂_mu A_ν − ∂_ν A_mu is the corresponding curvature/field-strength object.

This gives a useful structural pair:

connection → curvature
A_mu → F_muν

## Important distinction
Gauge redundancy is not itself a directly observable physical object. Different A_mu descriptions related by a gauge transformation represent the same physical electromagnetic configuration.

Therefore LIGHT must not identify "connection" with a physical material link without qualification.

## Architectural candidate
A useful abstraction is:

local state comparison → connection → accumulated difference → field strength → dynamics

The word "difference" here is mathematical: F_muν measures the antisymmetric derivative structure of the potential. It is not yet the Ω notion of difference.

## Strong clue
The theory does not obtain electromagnetic dynamics from an isolated scalar value. It requires relations between field values across spacetime, encoded through derivatives and the gauge connection.

This is a legitimate structural observation and a candidate bridge to RELATION-LAB.

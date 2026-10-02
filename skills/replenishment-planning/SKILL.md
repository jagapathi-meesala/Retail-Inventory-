---
name: replenishment-planning
description: Calculate deterministic retail replenishment quantities from current, reorder-point, and target-stock values.
---

# Replenishment Planning

## Purpose
Calculate a deterministic order quantity from current, reorder-point, and target-stock values.

## Inputs
Non-negative `current_stock`, `reorder_point`, and `target_stock`, with target at least as high as reorder point.

## Processing
Recommended quantity is `max(0, target_stock - current_stock)`.

## Outputs
Recommended quantity, action, and reason.

## Limitations
The calculation does not optimize for forecasted demand, lead time, pack size, budget, or supplier constraints.

## Expected behavior
The same inputs always produce the same result.

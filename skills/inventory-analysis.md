# Inventory Analysis

## Purpose
Classify current stock health from supplied SKU quantities and reorder points.

## Inputs
A non-empty list of objects with `sku`, `stock`, and `reorder_point`.

## Processing
Zero stock is critical; positive stock at or below reorder point is low; stock above reorder point is healthy.

## Outputs
Per-SKU status, shortfall, and aggregate status counts.

## Limitations
No demand forecast, seasonality, lead time, or supplier data is considered.

## Expected behavior
Invalid quantities and missing fields are rejected rather than guessed.

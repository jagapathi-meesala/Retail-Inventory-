# Explainability

## Inputs and Data Sources
Inputs are supplied as structured JSON-like objects containing SKU identifiers and inventory quantities such as current stock, reorder points, and target stock. The implementation uses only data supplied to the selected tool; there is no hidden database, web feed, or external retail data source.

### Input Requirements
Inventory analysis requires a non-empty `items` list with `sku`, `stock`, and `reorder_point`. Reorder recommendation requires non-negative `current_stock`, `reorder_point`, and `target_stock`, while stock summary requires `sku` and `stock`.

### Failure Handling
Missing fields, wrong types, negative quantities, empty collections, and inconsistent target/reorder values are rejected with structured validation errors. Unexpected execution failures are converted into a structured tool-failure response rather than silently returning a fabricated result.

## Decision and Reasoning
The decision logic is deterministic: an item is `critical` when stock is zero, `low` when stock is positive but at or below the reorder point, and `healthy` otherwise. The reorder quantity is `max(0, target_stock - current_stock)`, so the result is directly reproducible from the supplied quantities.

### Rules Applied
For inventory health, status is determined by comparing stock against zero and the reorder point. For replenishment, the agent recommends enough units to reach target stock and recommends no action when current stock already meets or exceeds target stock.

### Expected Outputs
Inventory analysis returns per-SKU status, stock, reorder point, shortfall, and aggregate counts. Reorder planning returns recommended quantity, action, and a concise reason; stock summary returns SKU count, total units, average units, and zero-stock SKUs.

### Worked Example
If current stock is 8 and target stock is 20, the recommended quantity is 12. If stock is 0 and reorder point is 5, the inventory status is `critical` and the shortfall is 5.

## Limits and Constraints
The agent does not estimate future demand, supplier lead time, seasonality, safety stock, promotions, or vendor constraints because those inputs are not implemented. It also does not execute purchases or modify an external inventory system.

### Constraints
Quantities must be non-negative numeric values and SKU identifiers must be non-empty strings. The reorder target must not be below the reorder point because that would contradict the contract used by the recommendation tool.

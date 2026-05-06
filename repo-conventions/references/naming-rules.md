# Naming Rules

Prefer repository-local convention first.

If unclear, use:

- `domain_responsibility_layer.ext`

Examples:

- `order_payment_service.py`
- `inventory_sync_job.ts`
- `billing_invoice_mapper.go`

Avoid standalone vague names:

- `utils`
- `helpers`
- `manager`
- `service`
- `handler`

Mirror the primary export whenever practical.

- `invoice_pdf_generator.py` -> `InvoicePdfGenerator`
- `billing_invoice_mapper.ts` -> `BillingInvoiceMapper`

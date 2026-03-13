import json
import random
import uuid
from datetime import datetime, timedelta

def generate_data():
    # Setup constants
    NUM_PROJECTS = 60
    NUM_RECEIVABLES = 1500
    NUM_PAYABLES = 1800
    NUM_TREASURY = 4000
    
    START_DATE = datetime.now() - timedelta(days=210)
    
    # 1. Generate Content Metadata (With Overruns)
    projects = []
    genres = ["DRAMA", "THRILLER", "COMEDY", "CRICKET", "REALITY", "ACTION"]
    content_types = ["ORIGINAL_SERIES", "LICENSED_MOVIE", "SPORTS_EVENT", "DOCUMENTARY", "SHORT_FORM"]
    tiers = ["TENTPOLE", "MID_BUDGET", "LOW_BUDGET"]
    statuses = ["DEVELOPMENT", "PRE_PRODUCTION", "FILMING", "POST_PRODUCTION", "RELEASED"]
    
    for i in range(NUM_PROJECTS):
        p_code = f"SL_PROJ_{100+i}"
        budget = random.randint(500000, 5000000)
        # 15% chance of a budget overrun
        if random.random() < 0.15:
            spend = budget * random.uniform(1.05, 1.30)
        else:
            spend = budget * random.uniform(0.40, 0.95)
            
        projects.append({
            "project_code": p_code,
            "title": f"Media Title {i+1}",
            "content_type": random.choice(content_types),
            "genre": random.choice(genres),
            "production_tier": random.choice(tiers),
            "production_status": random.choice(statuses),
            "primary_language": random.choice(["Hindi", "Tamil", "Telugu", "Marathi", "English"]),
            "target_regions": random.sample(["India", "US", "UK", "UAE", "Singapore"], k=random.randint(1, 3)),
            "release_date": (START_DATE + timedelta(days=random.randint(0, 210))).strftime("%Y-%m-%d"),
            "estimated_total_budget": budget,
            "actual_spend_to_date": int(spend)
        })

    # 2. Generate Accounts Receivable (AR) (With Silent Delays)
    receivables = []
    revenue_streams = ["ADVERTISING", "SYNDICATION", "DISTRIBUTION", "SPONSORSHIP"]
    customers = [
        {"id": "C_001", "name": "GroupM"},
        {"id": "C_002", "name": "Publicis"},
        {"id": "C_003", "name": "Dentsu"},
        {"id": "C_004", "name": "Omnicom"},
        {"id": "C_005", "name": "Netflix Licensing"},
        {"id": "C_006", "name": "Amazon Prime Distribution"}
    ]
    ar_status_options = ["OPEN", "PARTIALLY_PAID", "PAID", "OVERDUE", "DISPUTED"]
    
    for i in range(NUM_RECEIVABLES):
        inv_id = f"INV-{10000+i}"
        cust = random.choice(customers)
        inv_date = START_DATE + timedelta(days=random.randint(0, 180))
        terms = random.choice([30, 45, 60])
        due_date = inv_date + timedelta(days=terms)
        base = random.randint(5000, 150000)
        tax = base * 0.18
        
        status = random.choice(ar_status_options)
        if (datetime.now() - due_date).days > 0 and status == "OPEN":
            status = "OVERDUE"

        # Simulate "Silent Delay": Historical is consistently worse than contracted
        hist_delay = terms + random.randint(2, 20) if random.random() < 0.4 else terms + random.randint(-2, 2)

        receivables.append({
            "invoice_id": inv_id,
            "customer_id": cust["id"],
            "customer_name": cust["name"],
            "revenue_stream": random.choice(revenue_streams),
            "invoice_date": inv_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "contracted_payment_terms": terms,
            "base_amount": base,
            "tax_amount": tax,
            "total_amount": base + tax,
            "currency": "INR",
            "reporting_currency_code": "USD",
            "reporting_currency_total_amount": (base + tax) / 83.0,
            "exchange_rate": 83.0 + random.uniform(-1, 1),
            "status": status,
            "historical_avg_payment_days": hist_delay,
            "source_system": "NetSuite",
            "created_at": inv_date.isoformat(),
            "updated_at": datetime.now().isoformat(),
            "version": 1
        })

    # 3. Generate Accounts Payable (AP) (With Semantic Variations)
    payables = []
    vendors = [
        {"id": "V_001", "names": ["Amazon Web Services", "AWS", "AMAZON PAYMENTS"]},
        {"id": "V_002", "names": ["Akamai Technologies", "AKAMAI CDN"]},
        {"id": "V_003", "names": ["Red Chillies VFX", "RC VFX STUDIO"]},
        {"id": "V_004", "names": ["Dharma Productions", "DHARMA PROD"]},
        {"id": "V_005", "names": ["Facebook Ads", "META ADS", "FACEBOOK"]},
        {"id": "V_006", "names": ["Google Ads", "GOOGLE ADWORDS", "GOOGLE"]},
        {"id": "V_007", "names": ["Local Talent Agency", "TALENT UNLIMITED"]}
    ]
    ap_status_options = ["PENDING_APPROVAL", "APPROVED", "SCHEDULED_FOR_PAYMENT", "PAID"]
    
    for i in range(NUM_PAYABLES):
        bill_id = f"BILL-{20000+i}"
        vendor_data = random.choice(vendors)
        vendor_name = random.choice(vendor_data["names"]) # Semantic variation
        proj = random.choice(projects)
        inv_date = START_DATE + timedelta(days=random.randint(0, 190))
        terms = random.choice([30, 45, 60])
        due_date = inv_date + timedelta(days=terms)
        base = random.randint(1000, 70000)
        tax = base * 0.18
        
        payables.append({
            "bill_id": bill_id,
            "vendor_id": vendor_data["id"],
            "vendor_name": vendor_name,
            "spend_category": random.choice(["TECH_INFRASTRUCTURE", "CONTENT_PRODUCTION", "MARKETING", "TALENT_ROYALTIES"]),
            "project_code": proj["project_code"],
            "invoice_date": inv_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "base_amount": base,
            "tax_amount": tax,
            "total_amount": base + tax,
            "currency": "INR",
            "reporting_currency_code": "USD",
            "reporting_currency_total_amount": (base + tax) / 83.0,
            "exchange_rate": 83.0,
            "status": random.choice(ap_status_options),
            "source_system": "SAP",
            "created_at": inv_date.isoformat(),
            "updated_at": datetime.now().isoformat(),
            "version": 1
        })

    # 4. Generate Treasury Ledger (The "Hard Problems" Layer)
    treasury = []
    sources = [
        {"id": "BANK_HDFC_001", "type": "BANK_ACCOUNT", "entity": "SonyLiv India"},
        {"id": "BANK_HSBC_001", "type": "BANK_ACCOUNT", "entity": "Sony Global"},
        {"id": "STRIPE_INR", "type": "PAYMENT_GATEWAY", "entity": "SonyLiv India"},
        {"id": "APPLE_STORE", "type": "APP_STORE_MERCHANT", "entity": "Sony Global"}
    ]
    
    # Process PAID Receivables
    for ar in [ar for ar in receivables if ar["status"] == "PAID"]:
        source = random.choice(sources)
        txn_date = datetime.fromisoformat(ar["invoice_date"]) + timedelta(days=ar["historical_avg_payment_days"])
        
        # Scenario: Partial payment / Fee discrepancy (Hard Problem)
        real_amount = ar["total_amount"]
        if random.random() < 0.05: real_amount -= 150 # Customer short-paid
        
        # Scenario: Missing Reconciliation Ref (Data Quality Problem)
        ref = ar["invoice_id"] if random.random() > 0.10 else None
        
        treasury.append({
            "entry_id": f"TXN-{uuid.uuid4().hex[:8].upper()}",
            "liquidity_source_id": source["id"],
            "source_type": source["type"],
            "legal_entity": source["entity"],
            "transaction_date": txn_date.isoformat(),
            "settlement_status": "SETTLED" if random.random() > 0.02 else "FAILED",
            "amount_gross": real_amount,
            "platform_fees": real_amount * 0.02 if source["type"] == "PAYMENT_GATEWAY" else 0,
            "amount_net": real_amount * 0.98 if source["type"] == "PAYMENT_GATEWAY" else real_amount,
            "currency": "INR",
            "reconciliation_ref": ref,
            "entry_type": "INFLOW",
            "is_intercompany": False,
            "source_system": "Platform-API",
            "created_at": txn_date.isoformat(),
            "counterparty": {"id": ar["customer_id"], "name": ar["customer_name"], "type": "CUSTOMER"}
        })

    # Process PAID Payables
    for ap in [ap for ap in payables if ap["status"] == "PAID"]:
        source = random.choice([s for s in sources if s["type"] == "BANK_ACCOUNT"])
        txn_date = datetime.fromisoformat(ap["due_date"]) - timedelta(days=random.randint(0, 5))
        
        # Scenario: Duplicate Payment (CFO Nightmare)
        num_payments = 2 if random.random() < 0.005 else 1
        for _ in range(num_payments):
            treasury.append({
                "entry_id": f"TXN-OUT-{uuid.uuid4().hex[:8].upper()}",
                "liquidity_source_id": source["id"],
                "source_type": source["type"],
                "legal_entity": source["entity"],
                "transaction_date": txn_date.isoformat(),
                "settlement_status": "SETTLED",
                "amount_gross": -ap["total_amount"],
                "amount_net": -ap["total_amount"],
                "currency": "INR",
                "reconciliation_ref": ap["bill_id"],
                "entry_type": "OUTFLOW",
                "is_intercompany": False,
                "source_system": "Bank-API",
                "created_at": txn_date.isoformat(),
                "counterparty": {"id": ap["vendor_id"], "name": ap["vendor_name"], "type": "VENDOR"}
            })

    # Scenario: Random Transfers and "Mystery" Fees (The Leakage Problem)
    for i in range(200):
        txn_date = START_DATE + timedelta(days=random.randint(0, 200))
        treasury.append({
            "entry_id": f"TXN-OTH-{i}",
            "liquidity_source_id": random.choice(sources)["id"],
            "source_type": "BANK_ACCOUNT",
            "legal_entity": "SonyLiv India",
            "transaction_date": txn_date.isoformat(),
            "settlement_status": "SETTLED",
            "amount_gross": random.choice([-500, -1500, -2500]), # Small recurring "Mystery" leakage
            "amount_net": -3000,
            "currency": "INR",
            "entry_type": "FEE_ADJUSTMENT",
            "is_intercompany": False,
            "source_system": "Manual-Entry",
            "created_at": txn_date.isoformat()
        })

    # Save to files
    for name, data in [('content_metadata', projects), ('accounts_receivable', receivables), ('accounts_payable', payables), ('treasury_ledger', treasury)]:
        with open(f'data/{name}.json', 'w') as f:
            json.dump(data, f, indent=2)

    print("Sophisticated Data generation complete. All 'Hard Problems' injected.")

if __name__ == "__main__":
    generate_data()

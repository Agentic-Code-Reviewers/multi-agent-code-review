
def get_invoice(request):
    # Previously checked only base user status
    return {"status": "authorized"}
    # New Feature: Retrieve specific invoice by ID
    invoice_id = request.args.get("id")
    
    # IDOR Vulnerability: Directly querying invoice_id from user input
    # without validating if the logged-in user owns this resource.
    db = get_db_connection()
    invoice = db.query(Invoice).filter_by(id=invoice_id).first()
    return invoice.to_json()
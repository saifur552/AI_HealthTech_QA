# core_logic/billing_calculator.py

def calculate_patient_bill(consultation_fee, days_admitted, is_insured):
    """
    Calculates the total hospital bill for a patient.
    - Room charge is fixed at 1500 per day.
    - If insured, a 20% discount is applied to the subtotal.
    """
    room_charge_per_day = 1500
    total_room_cost = days_admitted * room_charge_per_day
    subtotal = consultation_fee + total_room_cost

    if is_insured:
        # Applying 20% insurance discount
        discount = subtotal * 0.20
        total = subtotal - discount
    else:
        total = subtotal
    
    return round(total, 2)
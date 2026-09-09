# tests/test_whitebox.py
import pytest
from core_logic.billing_calculator import calculate_patient_bill

def test_calculate_bill_with_insurance():
    # Consultation: 500, Days: 2 (Room: 3000), Subtotal: 3500
    # Insured True -> 20% off -> Expected: 2800.0
    result = calculate_patient_bill(500, 2, True)
    assert result == 2800.0

def test_calculate_bill_without_insurance():
    # Consultation: 500, Days: 2 (Room: 3000), Subtotal: 3500
    # Insured False -> Expected: 3500.0
    result = calculate_patient_bill(500, 2, False)
    assert result == 3500.0

def test_calculate_bill_rounding():
    # Consultation: 500.126, Days: 1 (Room: 1500), Subtotal: 2000.126
    # No insurance -> Expected rounding to 2 decimal places: 2000.13
    result = calculate_patient_bill(500.126, 1, False)
    assert result == 2000.13
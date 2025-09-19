def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """
    Convert an amount from one currency to another using exchange rates.
    
    Args:
        amount (float): The amount to convert
        from_currency (str): The source currency code (e.g., 'USD', 'EUR')
        to_currency (str): The target currency code (e.g., 'USD', 'EUR')
        exchange_rates (dict): Dictionary with currency pairs as keys and rates as values
    
    Returns:
        float: The converted amount, or None if conversion is not possible
    
    Raises:
        ValueError: If currencies are not found in exchange rates
    """
    # Check if both currencies exist in exchange rates
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError(f"One or both currencies ({from_currency}, {to_currency}) not found in exchange rates")
    
    # If converting to the same currency, return the original amount
    if from_currency == to_currency:
        return amount
    
    # Get the exchange rate for the currency pair
    rate_key = f"{from_currency}_{to_currency}"
    
    # Check if direct rate exists
    if rate_key in exchange_rates:
        return amount * exchange_rates[rate_key]
    
    # Check if reverse rate exists and calculate inverse
    reverse_key = f"{to_currency}_{from_currency}"
    if reverse_key in exchange_rates:
        return amount / exchange_rates[reverse_key]
    
    # If no direct conversion, try to convert through USD as base currency
    if from_currency != 'USD' and to_currency != 'USD':
        try:
            # Convert from source currency to USD
            usd_amount = convert_currency(amount, from_currency, 'USD', exchange_rates)
            # Convert from USD to target currency
            if usd_amount is not None:
                return convert_currency(usd_amount, 'USD', to_currency, exchange_rates)
        except ValueError:
            pass
    
    raise ValueError(f"Cannot convert from {from_currency} to {to_currency} with available rates")


def get_exchange_rates():
    """
    Get a sample dictionary of exchange rates.
    This is just for demonstration - in real applications, you would fetch current rates from an API.
    
    Returns:
        dict: Dictionary of exchange rates
    """
    return {
        'USD_EUR': 0.85,
        'USD_GBP': 0.73,
        'USD_JPY': 110.0,
        'USD_CAD': 1.25,
        'USD_AUD': 1.35,
        'USD_CHF': 0.92,
        'EUR_USD': 1.18,
        'EUR_GBP': 0.86,
        'EUR_JPY': 129.4,
        'GBP_USD': 1.37,
        'GBP_EUR': 1.16,
        'JPY_USD': 0.0091,
        'JPY_EUR': 0.0077,
        'CAD_USD': 0.80,
        'AUD_USD': 0.74,
        'CHF_USD': 1.09
    }


# Example usage and testing
if __name__ == "__main__":
    # Get sample exchange rates
    rates = get_exchange_rates()
    
    # Test conversions
    test_cases = [
        (100, 'USD', 'EUR'),
        (50, 'EUR', 'GBP'),
        (1000, 'USD', 'JPY'),
        (75, 'GBP', 'USD'),
        (200, 'CAD', 'AUD')
    ]
    
    print("Currency Conversion Examples:")
    print("=" * 40)
    
    for amount, from_curr, to_curr in test_cases:
        try:
            result = convert_currency(amount, from_curr, to_curr, rates)
            print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
        except ValueError as e:
            print(f"Error converting {amount} {from_curr} to {to_curr}: {e}")
    
    print("\n" + "=" * 40)
    
    # Interactive conversion
    print("\nInteractive Currency Converter:")
    print("Enter 'quit' to exit")
    
    while True:
        try:
            user_input = input("\nEnter amount, from currency, to currency (e.g., 100 USD EUR): ").strip()
            
            if user_input.lower() == 'quit':
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Please enter: amount from_currency to_currency")
                continue
            
            amount = float(parts[0])
            from_curr = parts[1].upper()
            to_curr = parts[2].upper()
            
            result = convert_currency(amount, from_curr, to_curr, rates)
            print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

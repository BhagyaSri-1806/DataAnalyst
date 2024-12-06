def calculate_ace_probability():
    # Initial probabilities
    total_cards = 52
    total_aces = 4
    
    # Probability of first ace
    prob_first_ace = total_aces / total_cards
    
    # Probability of second ace (given we drew first ace)
    prob_second_ace = (total_aces - 1) / (total_cards - 1)
    
    # Total probability (multiplication rule)
    total_probability = prob_first_ace * prob_second_ace
    
    print(f"Probability of drawing first ace: {prob_first_ace:.4f}")
    print(f"Probability of drawing second ace: {prob_second_ace:.4f}")
    print(f"Probability of drawing two aces: {total_probability:.4f}")

calculate_ace_probability(), 
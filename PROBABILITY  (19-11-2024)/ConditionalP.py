#... existing code ...

def conditional_probability(event_a, event_b, sample_space):
    """
    Calculate P(A|B) - the probability of event A given that event B has occurred
    
    Args:
        event_a: list of outcomes in event A
        event_b: list of outcomes in event B
        sample_space: list of all possible outcomes
    
    Returns:
        float: conditional probability P(A|B)
    """
    # Calculate intersection of events A and B
    intersection = set(event_a).intersection(set(event_b))
    
    # Calculate probabilities
    prob_b = len(event_b) / len(sample_space)
    prob_intersection = len(intersection) / len(sample_space)
    
    # P(A|B) = P(A∩B) / P(B)
    if prob_b == 0:
        return 0
    return prob_intersection / prob_b

# Example usage
if __name__ == "__main__":
    # Example with dice rolls
    sample_space = [(i, j) for i in range(1, 7) for j in range(1, 7)]  # All possible outcomes of rolling 2 dice
    event_a = [(i, j) for i, j in sample_space if i + j > 7]  # Sum greater than 7
    event_b = [(i, j) for i, j in sample_space if i == j]     # Double rolls
    
    prob = conditional_probability(event_a, event_b, sample_space)
    print(f"\nP(Sum > 7 | Double Roll) = {prob:.3f}")

#... existing code ...
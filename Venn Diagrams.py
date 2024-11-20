# ... existing ace probability code ...

def draw_venn_diagram(set_a, set_b, label_a="A", label_b="B"):
    """
    Draw a Venn diagram for two sets using matplotlib.
    
    Args:
        set_a: First set of elements
        set_b: Second set of elements
        label_a: Label for first set (default: "A")
        label_b: Label for second set (default: "B")
    """
    import matplotlib.pyplot as plt
    from matplotlib_venn import venn2
    
    # Create figure and axis
    plt.figure(figsize=(10, 6))
    
    # Create Venn diagram
    venn2([set(set_a), set(set_b)], 
          set_labels=(label_a, label_b))
    
    plt.title("Venn Diagram")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example sets
    numbers_div_by_2 = {2, 4, 6, 8, 10}
    numbers_div_by_3 = {3, 6, 9, 12}
    
    draw_venn_diagram(numbers_div_by_2, numbers_div_by_3, 
                     "Divisible by 2", "Divisible by 3")
    
def parrot(sound="Squawk!"):
    """Return a parrot sound."""
    print(sound)
    return sound

# Example usage
result = parrot() # Uses default argument
print("Returned:", result)

result = parrot("Hello!") # Uses provided argument
print("Returned:", result)

    
    

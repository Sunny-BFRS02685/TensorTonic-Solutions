import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    X = np.asarray(x, dtype=float)
    print(X)
    centered = X - np.mean(X)
    print(centered)
    variance = float(np.sum(centered ** 2) / (X.size - 1))
    print(variance)
    sd = float(np.sqrt(variance))
    return {
        "variance": variance,
        "standard_deviation": sd
    }
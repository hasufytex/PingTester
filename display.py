from tabulate import tabulate

def display_results_in_table(results):
    """Displays the ping results in a formatted table with a delta column."""
    # Add the "Delta (ms)" header
    table = tabulate(results, headers=["Name", "Ping (ms)", "Delta (ms)", "Status"], tablefmt="grid")
    print("\033c", end="")  # Clear terminal
    print(table)

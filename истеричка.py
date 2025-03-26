def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    if 0 in opponent_history:
        i = len(my_history)
        return (sum(my_history) + sum(opponent_history) + i) % 2
    return 1
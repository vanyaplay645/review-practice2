def sum_list(numbers):
    """Возвращает сумму всех чисел. Пустой список → 0."""
    total = 0
    for n in numbers:
        total += n
    return total
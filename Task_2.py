cook_book = {
    dish: {"name": name, "quantity": quantity, "measure": measure}
    for dish, _, *indigrients in map(str.splitlines, open("input.txt").read().split("\n\n"))
    for name, quantity, measure in map(lambda x: x.rsplit(" | ", 2), indigrients)
}
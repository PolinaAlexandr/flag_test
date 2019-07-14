def add_border(line: str) -> str:
    return f"#{line}#"


def construct_line(line_number: int, n: int) -> str:
    empty_height: int = int(n / 2)
    inner_width: int = 3 * n
    if line_number < empty_height:
        return add_border(' ' * inner_width)

    line_half_length: int = int(inner_width / 2)
    circle_number: int = line_number - empty_height

    line_half: str = (
        f"{(n + (line_half_length - n - circle_number - 1)) * ' '}"
        f"*{circle_number * 'o'}"
    )
    line: str = f"{line_half}{line_half[::-1]}"

    return add_border(line)


def flag(n: int) -> str:
    flag_half: str = '\n'.join(
        construct_line(line_number, n)
        for line_number in range(n)
    )
    flag: str = f"{flag_half}\n{flag_half[::-1]}"
    inner_width: int = 3 * n
    flag_with_borders: str = (
        f"{'#' * (inner_width + 2)}\n"
        f"{flag}\n"
        f"{'#' * (inner_width + 2)}"
    )
    return flag_with_borders


print(flag(4))
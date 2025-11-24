students_marks = [30, 20, 15, 18, 31, 35, 40, 45, 10, 5, 16]
INVALID_MSG = "Invalid values in the students marks list"


def normalize_marks(marks):
    """Return a list of floats parsed from the incoming marks."""
    normalized = []
    for mark in marks:
        if isinstance(mark, (int, float)):
            normalized.append(float(mark))
            continue
        if isinstance(mark, str):
            candidate = mark.strip()
            if not candidate:
                raise ValueError(INVALID_MSG)
            try:
                normalized.append(float(candidate))
            except ValueError as exc:  # pragma: no cover - informative branch
                raise ValueError(INVALID_MSG) from exc
            continue
        raise ValueError(INVALID_MSG)
    if not normalized:
        raise ValueError("Marks list must not be empty.")
    return normalized


def marks_above_mean(marks):
    """
    Calculate the mean of marks and return values above it.

    Args:
        marks: Iterable of numeric scores (ints/floats/convertible strings).

    Returns:
        Tuple of (mean, list of marks greater than mean).
    """
    normalized = normalize_marks(marks)
    mean_value = sum(normalized) / len(normalized)
    above_mean = [mark for mark in normalized if mark > mean_value]
    return mean_value, above_mean


def _format_number(value):
    return (
        str(int(value))
        if isinstance(value, float) and value.is_integer()
        else f"{value:.2f}".rstrip("0").rstrip(".")
    )


def format_mean_output(mean_value, above_mean):
    """Format the result string to match the requested output."""
    mean_str = _format_number(mean_value)
    above_str = (
        ",".join(_format_number(mark) for mark in above_mean) if above_mean else "None"
    )
    return (
        f"Mean value = {mean_str}, "
        f"Students marks greater than the mean value i.e {mean_str} = {above_str}"
    )


if __name__ == "__main__":
    try:
        mean, above = marks_above_mean(students_marks)
        print(format_mean_output(mean, above))
        students_marks.append('1')
        mean, above = marks_above_mean(students_marks)
        print(format_mean_output(mean, above))
        students_marks.append('-')
        mean, above = marks_above_mean(students_marks)
        print(format_mean_output(mean, above))
    except ValueError as error:
        print(error)
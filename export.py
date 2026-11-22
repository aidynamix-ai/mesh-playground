def _needs_quoting(text):
    for ch in text:
        if ch in ",\"\r\n":
            return True
    return False


def _format_field(value):
    text = value if isinstance(value, str) else str(value)
    if _needs_quoting(text):
        return '"' + text.replace('"', '""') + '"'
    return text


def export_csv(rows):
    if not rows:
        return ""
    keys = list(rows[0].keys())
    lines = [",".join(_format_field(k) for k in keys)]
    for row in rows:
        lines.append(",".join(_format_field(row[k]) for k in keys))
    return "\n".join(lines)

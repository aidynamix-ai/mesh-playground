import export

assert callable(export.export_csv)


def test_header_key_order_and_bare_values():
    assert export.export_csv([{"a": "1", "b": "x"}]) == "a,b\n1,x"


def test_empty_input():
    assert export.export_csv([]) == ""


def test_value_with_comma_is_quoted():
    assert export.export_csv([{"a": "1", "b": "x,y"}]) == 'a,b\n1,"x,y"'


def test_value_with_double_quotes_is_doubled():
    assert export.export_csv([{"a": 'he said "hi"', "b": "plain"}]) == 'a,b\n"he said ""hi""",plain'


def test_value_with_newline_is_quoted():
    assert export.export_csv([{"a": "line1\nline2", "b": 2}]) == 'a,b\n"line1\nline2",2'


def test_value_with_crlf_is_quoted():
    assert export.export_csv([{"a": "top\r\nbottom", "b": "c"}]) == 'a,b\n"top\r\nbottom",c'


def test_value_with_carriage_return_is_quoted():
    assert export.export_csv([{"a": "a\rb", "b": "c"}]) == 'a,b\n"a\rb",c'


def test_multiple_rows_in_list_order():
    rows = [
        {"a": "1", "b": "x"},
        {"a": "2", "b": "y"},
        {"a": "3", "b": "z"},
    ]
    assert export.export_csv(rows) == "a,b\n1,x\n2,y\n3,z"


def test_non_string_scalars_render_via_str():
    row = {"i": 42, "f": 3.14, "n": None, "t": True}
    assert export.export_csv([row]) == "i,f,n,t\n42,3.14,None,True"


def test_no_trailing_newline():
    out = export.export_csv([{"a": "1"}])
    assert out == "a\n1"
    assert not out.endswith("\n")


def test_header_keys_use_same_quoting_rule():
    assert export.export_csv([{"a,b": "1"}]) == '"a,b"\n1'


for _test in (
    test_header_key_order_and_bare_values,
    test_empty_input,
    test_value_with_comma_is_quoted,
    test_value_with_double_quotes_is_doubled,
    test_value_with_newline_is_quoted,
    test_value_with_crlf_is_quoted,
    test_value_with_carriage_return_is_quoted,
    test_multiple_rows_in_list_order,
    test_non_string_scalars_render_via_str,
    test_no_trailing_newline,
    test_header_keys_use_same_quoting_rule,
):
    _test()

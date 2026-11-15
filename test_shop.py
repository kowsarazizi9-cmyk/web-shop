def test_find_case_insensitive():
    assert [p.sku for p in find_by_name(products, "KEY")] == ["B2"]
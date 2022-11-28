from shop_app import product

def test_include_column_names():
    empty_list = []
    empty_description = []
    assert isinstance(product.include_column_names(empty_list,empty_description),list)

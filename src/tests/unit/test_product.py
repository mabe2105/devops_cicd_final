from shop_app import product

def test_include_column_names():
    empty_list = []
    empty_description = []
    assert isinstance(product.include_column_names(empty_list,empty_description),list)

def test_return_pickle_rick_placeholders():
    our_names = product.return_pickle_rick_placeholders()
    assert our_names == {"names": "Rick & Morty"}
    #inner loop will fail
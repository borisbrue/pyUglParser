from Uglparser import Uglparser

ugl_file = Uglparser("./tests/raw/dummy.001")


print(ugl_file.get_meta()["kundennummer"] == "005627")


print(len(ugl_file.get_products()) == 16)

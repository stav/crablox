from blocks import block


def index_block(rt):

    path = "/index"

    @rt(path)
    def get():
        return "Hello, World!"

    return block(path, "hello", "Hello")

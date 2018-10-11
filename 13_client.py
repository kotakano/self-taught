class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self.unsafe = "unsafe"

    def public_method(self):
        # client が使っても良い
        pass    # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method(self):
        " client は使うべきじゃない"
        pass    # pass文は、文が必須な公文で何もしない場合に使う

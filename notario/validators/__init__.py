

class cherry_pick(tuple):
    """
    This is not really a validator, but will allow one to make
    sure just certain keys (as defined in ``must_validate`` are
    validated. The engine will discard all others that are not
    defined here.

    It should be used in the same manner as when constructing
    a schema, but instead of a regular tuple, this should be used.

    .. note::
        If ``must_validate`` is not defined with any items, it will
        generate them with the items on the tuple passed in if possible, unless
        the tuple created is not a key value pair.

    """
    must_validate = ()

    def __init__(self, _tuple):
        try:
            self.must_validate = tuple([key for key, value in _tuple])
        except ValueError:  # single k/v pair
            if len(_tuple) == 2:
                self.must_validate = tuple(_tuple[0])
        return super(cherry_pick, self).__init__()

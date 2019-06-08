import abc


class Filter(abc.ABC):
    """Use for creating filter classes

    Args:
        `key` (str): the unique filter identification

    Methods:
        `apply`: apply filter for objects
        `apply_dict_params`: the same as `apply` but get filter param from params dict
    """
    def __init__(self, key: str):
        self.key = key

    def apply(self, objects, param):
        return self._execute(objects, param)

    def apply_dict_params(self, objects, params: dict):
        if self.key in params:
            objects = self._execute(objects, params[self.key])
        return objects

    @abc.abstractmethod
    def _execute(self, objects, param):
        return objects

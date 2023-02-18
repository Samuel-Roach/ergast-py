""" Base model class """


class BaseModel:
    def __repr__(self) -> str:
        attrs = ', '.join(f"{key}={value}" for key, value in vars(self).items())
        return f"{type(self).__name__}({attrs})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, type(self)) and all(
            getattr(self, key) == getattr(__o, key) for key in vars(self)
        )

    def __str__(self) -> str:
        attrs = '\n\t'.join(f"{key}: {value}" for key, value in vars(self).items())
        return f"{type(self).__name__} (\n\t{attrs}\n)"

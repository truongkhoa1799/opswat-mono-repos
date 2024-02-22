from pydantic import BaseModel


class BaseEntity(BaseModel):
    @classmethod
    def from_dict(cls, data):
        """ Convert data from a dictionary
        """
        return cls(**data)

    def to_dict(self):
        """ Convert data into dictionary
        """
        return self.model_dump()

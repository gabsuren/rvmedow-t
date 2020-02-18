from abc import ABC, abstractmethod
import random
import pickle
import os


class PersistentLayer(ABC):
    @abstractmethod
    def get(self, id):
        raise NotImplemented

    @abstractmethod
    def save(self):
        raise NotImplemented


class FileSystem(PersistentLayer):
    """FileSystem class.

        Attributes:
            id(Int) ID of object
    """
    id = 0

    def get(self, _id):
        with open(f'base_directory/{self._id}', 'rb') as f:
            obj = pickle.load(f)
            return obj

    def save(self):
        self.id = random.randint(1, 1000000)
        with open(f'base_directory/{self.id}', 'ab') as f:
            pickle.dump(self, f)
            f.close()

    def update(self):
        obj = self.get(self.id)
        obj.save()

    def delete(self):
        os.remove(f'../base_directory/{self.id}')


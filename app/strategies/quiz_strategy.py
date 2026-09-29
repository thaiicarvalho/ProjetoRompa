from abc import ABC
from abc import abstractmethod


class QuizStrategy(ABC):

    @abstractmethod
    def avaliar(self, percentual):

        pass
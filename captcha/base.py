from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class CaptchaResult:
    id: str
    question: str
    answer: str
    payload: any
    
class BaseCaptcha(ABC):
    
    @abstractmethod
    def generate(self) -> CaptchaResult:
        """ generate a new captcha """
        pass
    
    @abstractmethod
    def validate(self, user_input: str, stored_answer: str) -> bool:
        """ Validate user input against stored answer """
        pass        
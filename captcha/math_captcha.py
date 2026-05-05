from .base import BaseCaptcha, CaptchaResult
import random
import uuid

class MathCaptcha(BaseCaptcha):
    def __init__(self, min_val=1, max_val=10):
        """ init for min and max math number """
        
        self.min_val = min_val
        self.max_val = max_val
        
    def generate(self) -> CaptchaResult:
        """ generate math question """
        
        num_a = random.randint(self.min_val, self.max_val)
        num_b = random.randint(self.min_val, self.max_val)
        op = random.choice(['+', '-'])
        question = f"{num_a} {op} {num_b}"
        answer = str(eval(question))
        
        return CaptchaResult(
            id=str(uuid.uuid4()),
            question=question,
            answer=answer,
            payload=None
        )

    def validate(self, user_input: str, stored_answer: str) -> bool:
        return user_input.strip() == stored_answer.strip()
    

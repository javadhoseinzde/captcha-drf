from .base import BaseCaptcha, CaptchaResult
import random
import uuid
import os

class ImageCaptcha(BaseCaptcha):
    def __init__(self, image_count: int, image_path: str):
        """ init for min and max math number """
        
        self.image_count = image_count
        self.image_path = image_path
        
    def generate(self) -> CaptchaResult:
        """ generate math question """
        
        dirs = os.listdir("dataset")
        directory_list = [d for d in dirs if d != ".DS_Store"]
        correct_answer_dir = random.choice(directory_list)
        
        captcha = {}
        answer = []
        for dirs in directory_list:
        
            if correct_answer_dir == dirs:
                captcha["answer"] = os.listdir("dataset/" + dirs)
                answer.append(os.listdir("dataset/" + dirs))
            else:
                image_name = random.choice(os.listdir("dataset/" + dirs))
                captcha[dirs] = image_name      
                  
        return CaptchaResult(
            id=str(uuid.uuid4()),
            question=captcha,
            answer=os.listdir("dataset/" + dirs),
            payload=None
        )

    def validate(self, user_input: str, stored_answer: str) -> bool:
        return user_input.strip() == stored_answer.strip()
    

print(ImageCaptcha(image_count=1, image_path=1).generate())

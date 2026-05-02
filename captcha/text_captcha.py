import random, string, io
import uuid
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from .base import BaseCaptcha, CaptchaResult

class TextCaptcha(BaseCaptcha):
    """ this Class make thie TextCaptcha Image """
    def __init__(self, length=5, width=200, height=80, fonts=None):
        self.length = length
        self.width = width
        self.height = height
        self.fonts = fonts or ["assets/Roboto-Bold.ttf"]

    def _random_text(self):
        """ this method create random character """
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=self.length))

    def generate(self) -> CaptchaResult:
        """ this method create captcha image """
        text = self._random_text()
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(random.choice(self.fonts), 40)

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (self.width - text_width) / 2 - bbox[0]
        y = (self.height - text_height) / 2 - bbox[1]

        draw.text((x, y), text, font=font, fill=(0, 0, 0))
        draw.text((x, y), text, font=font, fill=(0, 0, 0))

        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
        return CaptchaResult(
            id=str(uuid.uuid4()),
            question="",
            answer=text,
            payload=buffer.read()
        )

    def validate(self, user_input: str, stored_answer: str) -> bool:
        return user_input.strip().upper() == stored_answer.upper()
    
captcha_generator = TextCaptcha()
captcha_result = captcha_generator.generate()

with open(f"captcha_{captcha_result.id}.png", "wb") as f:
    f.write(captcha_result.payload)

print(f"Captcha image saved as captcha_{captcha_result.id}.png")
print(f"The answer is: {captcha_result.answer}")
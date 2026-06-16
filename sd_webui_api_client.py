import base64, io, requests
from PIL import Image

class SDClient:
    def __init__(self, url="http://localhost:7860"):
        self.url = url.rstrip("/")

    def txt2img(self, prompt, negative="", steps=30, cfg=7.5, w=512, h=512, seed=-1):
        r = requests.post(f"{self.url}/sdapi/v1/txt2img", json={"prompt": prompt, "negative_prompt": negative, "steps": steps, "cfg_scale": cfg, "width": w, "height": h, "seed": seed})
        r.raise_for_status()
        return self._dec(r.json()["images"][0])

    def img2img(self, img, prompt, negative="", strength=0.75, steps=30):
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        r = requests.post(f"{self.url}/sdapi/v1/img2img", json={"init_images": [base64.b64encode(buf.getvalue()).decode()], "prompt": prompt, "negative_prompt": negative, "denoising_strength": strength, "steps": steps})
        r.raise_for_status()
        return self._dec(r.json()["images"][0])

    def _dec(self, b64):
        return Image.open(io.BytesIO(base64.b64decode(b64)))

    def progress(self):
        return requests.get(f"{self.url}/sdapi/v1/progress").json()

if __name__ == "__main__":
    c = SDClient()
    print("Generating...")
    c.txt2img("a beautiful sunset over the ocean").save("test.png")
    print("Saved: test.png")

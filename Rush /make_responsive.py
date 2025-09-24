from PIL import Image
import os

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images', 'camp.png'))
OUT_DIR = os.path.dirname(SRC)
SIZES = [800, 1600, 4000]

def main():
    if not os.path.exists(SRC):
        print('Source image not found:', SRC)
        return
    img = Image.open(SRC)
    base_name = 'camp'
    for w in SIZES:
        h = int(img.height * (w / img.width))
        out_path = os.path.join(OUT_DIR, f'{base_name}-{w}.png')
        resized = img.resize((w, h), Image.LANCZOS)
        resized.save(out_path, 'PNG', optimize=True)
        print('Wrote', out_path)

if __name__ == '__main__':
    main()
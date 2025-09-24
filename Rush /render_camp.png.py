from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'images', 'camp.png')
OUT = os.path.abspath(OUT)

W, H = 4000, 4000

def vertical_gradient(size, top_color, bottom_color):
    w, h = size
    base = Image.new('RGB', (w, h), top_color)
    top_r, top_g, top_b = top_color
    bot_r, bot_g, bot_b = bottom_color
    for y in range(h):
        t = y / (h - 1)
        r = int(top_r * (1 - t) + bot_r * t)
        g = int(top_g * (1 - t) + bot_g * t)
        b = int(top_b * (1 - t) + bot_b * t)
        ImageDraw.Draw(base).line([(0, y), (w, y)], fill=(r, g, b))
    return base

def main():
    # Colors
    c1 = (62, 120, 255)  # #3e78ff
    c2 = (0, 180, 255)   # #00b4ff

    img = vertical_gradient((W, H), c1, c2)
    draw = ImageDraw.Draw(img)

    # Draw rounded rect border (subtle)
    border = Image.new('RGBA', (W, H), (0,0,0,0))
    bd = ImageDraw.Draw(border)
    # center circle (face)
    cx, cy = W // 2, int(H * 0.33)
    cr = int(W * 0.195)
    bd.ellipse((cx-cr, cy-cr, cx+cr, cy+cr), fill=(255,255,255,230))

    # small mouth/neck rectangle
    bd.rectangle((cx - int(cr*0.9), cy + int(cr*0.45), cx + int(cr*0.9), cy + int(cr*0.9)), fill=(62,120,255,190))

    img = Image.alpha_composite(img.convert('RGBA'), border)
    draw = ImageDraw.Draw(img)

    # Draw initials TT
    try:
        # try common fonts; fall back to default
        font_large = ImageFont.truetype('arial.ttf', int(W * 0.18))
        font_name = ImageFont.truetype('arial.ttf', int(W * 0.03))
    except Exception:
        font_large = ImageFont.load_default()
        font_name = ImageFont.load_default()

    # center text
    txt = 'TT'
    try:
        bbox = draw.textbbox((0,0), txt, font=font_large)
        wtxt = bbox[2] - bbox[0]; htxt = bbox[3] - bbox[1]
    except Exception:
        wtxt, htxt = font_large.getsize(txt)
    draw.text((cx - wtxt/2, cy - htxt/2 - int(cr*0.05)), txt, fill=(62,120,255), font=font_large)

    # name
    name = 'Tranphakorn Taychatoh'
    try:
        bbox = draw.textbbox((0,0), name, font=font_name)
        wname = bbox[2] - bbox[0]; hname = bbox[3] - bbox[1]
    except Exception:
        wname, hname = font_name.getsize(name)
    draw.text((cx - wname/2, cy + cr + int(H*0.02)), name, fill=(255,255,255), font=font_name)

    # Ensure directory exists
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.convert('RGB').save(OUT, 'PNG', quality=95)
    print('Wrote', OUT)

if __name__ == '__main__':
    main()

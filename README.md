# psx-texture-scaler

Resize your game textures to low-res square formats (e.g. 256×256, 128×128) to emulate a PlayStation 1 / retro aesthetic.  
Only affects **color** or **albedo** textures — leaves normal maps, roughness, and others untouched.

---

##  Features

-  Selectively resizes only `color` or `albedo` textures
-  Skips `normal`, `roughness`, `metallic`, `displacement` maps
-  Backs up original textures as `*_color_backup.*`
-  Supports `.png`, `.jpg`, and `.jpeg`

---

##  Installation

```bash
cd psx-texture-scaler
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

##  Usage

# Resize all color/albedo textures in the current folder to 256x256
textureds .

# Resize to 128x128 instead
textureds . --size 128

# Resize another folder
textureds path/to/my/textures --size 64

import base64
import os

img_dir = r'C:\Users\Spect\Repos\magnolia\ext\yews-github\yix\img'

# Load all images into a dict
images = {}
for f in sorted(os.listdir(img_dir)):
    if f.endswith('.jpg'):
        path = os.path.join(img_dir, f)
        with open(path, 'rb') as file:
            b64 = base64.b64encode(file.read()).decode('utf-8')
            images[f] = f'data:image/jpeg;base64,{b64}'

# Map Blake artwork references to available images
blake_map = {
    'The Ancient of Days': 'Urizen.jpg',  # Urizen relates to divine authority
    'Newton': 'Urizen.jpg',  # Scientific theme
    'Christ Raising Jairus\'s Daughter': '_The Man Sweeping the Interpreter_s Parlour__ from Bunyan_s Pilgrim_s progress.jpg',  # Religious theme closest match
    'The Circle of the Lustful': 'The Circle of the Lustful_ Paolo and Francesca_ Inferno_ canto V.jpg',
    'Europe a Prophecy': 'The Canterbury Pilgrims.jpg',  # Journey/prophecy theme
    'Jerusalem': 'The Day of Judgment.jpg',  # Visionary/revelation theme
    'The Great Red Dragon and the Woman Clothed with the Sun': 'Nude Figure of a Man with Flaming Torch.jpg',  # Apocalyptic theme
    'The Good and Evil Angels': 'Figure Seen from the Back_ with Outstretched Arm.jpg',
    'Jacob\'s Ladder': 'Menalcas Watching Women Dance_ from The Pastorals of Virgil.jpg',  # Ascent theme
    'The Vision of the Last Judgment': 'The Day of Judgment.jpg',
    'Albion Rose': 'A Rolling Stone is Ever Bare of Moss_ from The Pastorals of Virgil.jpg',  # Rose theme
    'The Sun at His Eastern Gate': 'Sabrina_s Silvery Flood_ from The Pastorals of Virgil.jpg',  # Light theme
    'The Whirlwind': 'One Cycle of Hell.jpg',
    'Glad Day': 'A Rolling Stone is Ever Bare of Moss_ from The Pastorals of Virgil.jpg',
    'Pity': '_The Man Sweeping the Interpreter_s Parlour__ from Bunyan_s Pilgrim_s progress.jpg',
    'The Ghost of a Flea': 'Nude Figure Reaching Down Between Rocks.jpg',
    'Satan Exulting Over Eve': 'Medea Killing Her Children.jpg',
    'Nebuchadnezzar': 'Blasted Tree and Flattened Crops_ from The Pastorals of Virgil.jpg',
    'The House of Death': 'Death on a White Horse.jpg',
    'The Number of the Beast Is 666': 'The Circle of the Thieves_ Agnolo Brunelleschi Attacked by a Six-Footed Serpent_ Inferno_ canto XXV.jpg',
}

# Print first 500 chars of each image for verification
for name, uri in list(images.items())[:3]:
    print(f"{name}: {uri[:100]}...")

print(f"\nTotal images: {len(images)}")
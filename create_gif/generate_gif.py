import cv2
from PIL import Image
from tqdm import tqdm 

import os
from PIL import Image, ImageSequence




def create_gif(folder, pixel_size_w, pixel_size_h, number_of_frames, time_of_the_gif):
    images = []
    filenames = sorted([f for f in os.listdir(folder) if f.endswith((".png", ".jpg", ".jpeg"))])
    # Calcul du pas en fonction du nombre de frames demandé
    step = max(len(filenames) // number_of_frames, 1)
    # Sélection des fichiers correspondant à notre pas
    filenames = filenames[::step]
    for filename in filenames:
        # Ouverture et redimensionnement des images
        img = Image.open(os.path.join(folder, filename))
        if pixel_size_w != None:
            img = img.resize((pixel_size_h, pixel_size_w), Image.ANTIALIAS)
        images.append(img)
            
    # Calcul de la durée de chaque frame dans le gif
    frame_duration = time_of_the_gif * 1000 // len(images)  # Converti en ms

    # Création du GIF
    images[0].save('output.gif',
                   save_all=True, append_images=images[1:], optimize=False, duration=frame_duration, loop=0)


def resize_and_pad(img, target_size, fill_color=(0, 0, 0)):
    # D'abord, on redimensionne l'image
    img.thumbnail(target_size, Image.ANTIALIAS)
    
    # On crée une nouvelle image de la taille cible avec des bandes noires
    new_img = Image.new("RGB", target_size, fill_color)
    
    # On calcule les coordonnées du coin supérieur gauche de l'image pour la centrer
    y = (target_size[1] - img.size[1]) // 2
    x = (target_size[0] - img.size[0]) // 2

    # On colle l'image redimensionnée sur l'image de base
    new_img.paste(img, (x, y))
    
    return new_img

def create_gif_from_video(video_path, output_name, pixel_size_w, pixel_size_h, time_start, time_finish, number_of_frames, time_of_the_gif):
    # Ouvre la vidéo
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Obtient le nombre d'images par seconde

    # Calcule les frames de début et de fin
    start_frame = int(time_start * fps)
    end_frame = int(time_finish * fps)

    # Calcule le step entre chaque frame à prendre
    step = max((end_frame - start_frame) // number_of_frames, 1)  # Assure qu'on prend au moins une image

    images = []
    range_iter = range(start_frame, end_frame, step)
    for i in tqdm(range_iter):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:  # Si la lecture a réussi
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convertit l'image en RGB
            if pixel_size_w != None:
                # img = img.resize((pixel_size_h, pixel_size_w), Image.ANTIALIAS)
                img = resize_and_pad(img, (pixel_size_h, pixel_size_w), fill_color=(0, 0, 0))
            images.append(img)
            
    cap.release()

    # Calcule la durée de chaque frame dans le gif
    frame_duration = time_of_the_gif * 1000 // number_of_frames  # Converti en ms

    # Crée le gif
    images[0].save(output_name,
                   save_all=True, append_images=images[1:], optimize=False, duration=frame_duration, loop=0)


def create_gif_from_gif(gif_path, output_name, pixel_size_w = 680, pixel_size_h = 420, length_last_frame = 18):
    """
    Opens a GIF, resizes it while maintaining aspect ratio, adds black borders if necessary,
    and adjusts the duration of the last frame.

    Args:
    gif_path (str): Path to the input GIF file.
    output_name (str): Name of the output GIF file.
    pixel_size_w (int): Target width of the GIF in pixels.
    pixel_size_h (int): Target height of the GIF in pixels.
    length_last_frame (int): Duration of the last frame in frames.
    """
    # Open the GIF
    with Image.open(gif_path) as img:
        # Create frames while maintaining aspect ratio
        frames = []
        for frame in ImageSequence.Iterator(img):
            # Maintain aspect ratio
            frame = frame.convert('RGBA')  # Convert to RGBA to maintain transparency
            frame.thumbnail((pixel_size_w, pixel_size_h), Image.ANTIALIAS)

            # Create a new image with black background
            bordered_frame = Image.new('RGB', (pixel_size_w, pixel_size_h), 'black')
            # Calculate position to paste the original frame
            x = (pixel_size_w - frame.width) // 2
            y = (pixel_size_h - frame.height) // 2
            bordered_frame.paste(frame, (x, y), frame)  # Use frame as mask for transparency

            frames.append(bordered_frame)

        # Modify the duration of the last frame
        # frame_durations = [img.info['duration'] for _ in frames[:-1]]
        # frame_durations.append(img.info['duration'] * length_last_frame)
        frame_duration_per_frame = 130
        frame_durations = [frame_duration_per_frame for _ in frames[:-1]]
        frame_durations.append(frame_duration_per_frame * length_last_frame)

        # Save the modified frames as a new GIF
        frames[0].save(output_name, save_all=True, append_images=frames[1:], duration=frame_durations, loop=0)


# Example usage
create_gif_from_gif('assets/img/projects/ppgm/ppgm.gif', 'create_gif/ppgm.gif')



# video_path = 'chaseTag.mov'
# output_name = "GIF_chaseTag.gif"
# create_gif_from_video(video_path, output_name,420, 680,  0, 16, 90, 5)
# create_gif_from_video(video_path, 600, 0, 40, 100, 5)
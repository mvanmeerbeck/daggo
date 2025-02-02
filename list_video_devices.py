import cv2

def list_video_devices():
    # Liste des appareils de capture vidéo disponibles
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def open_video_device(device_index):
    # Ouvrir l'appareil de capture vidéo avec OpenCV
    cap = cv2.VideoCapture(device_index)
    
    if not cap.isOpened():
        print(f"Erreur : Impossible d'ouvrir l'appareil de capture vidéo {device_index}.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de lire le flux vidéo.")
            break
        
        # Traitement de l'image (par exemple, affichage de l'image)
        cv2.imshow('Video Stream', frame)
        
        # Quitter la boucle si 'q' est pressé
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libérer les ressources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    devices = list_video_devices()
    print("Appareils de capture vidéo disponibles : ", devices)
    
    if devices:
        # Ouvrir le premier appareil de capture vidéo disponible
        open_video_device(devices[0])
    else:
        print("Aucun appareil de capture vidéo disponible.")
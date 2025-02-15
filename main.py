import cv2
import mediapipe as mp

# Implementasi Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Fungsi untuk mengenali gesture tangan
def recognize_gesture(hand_landmarks):
    # Ambil posisi ujung jari
    ujung_jempol = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    ujung_telunjuk = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    ujung_tengah = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ujung_manis = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    ujung_kelingking = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    
    # Thumbs UP => jika hanya jempol diangkat
    if (ujung_jempol.y < ujung_telunjuk.y and
        ujung_jempol.y < ujung_tengah.y and
        ujung_jempol.y < ujung_manis.y and
        ujung_jempol.y < ujung_kelingking.y):
        return "Thumbs Up"
      
    # PEACE => Jika telunjuk & tengah diangkat
    if (ujung_telunjuk.y < ujung_manis.y and ujung_tengah.y < ujung_manis.y and  
        ujung_manis.y > ujung_tengah.y and ujung_kelingking.y > ujung_tengah.y and 
        ujung_jempol.y > ujung_tengah.y):
        return "Peace"
      
    # Metal => Jika Jempol, telunjuk & Kelingking diangkat
    if (ujung_jempol.y < ujung_tengah.y and ujung_jempol.y < ujung_manis.y and
        ujung_telunjuk.y < ujung_tengah.y and ujung_telunjuk.y < ujung_manis.y and
        ujung_kelingking.y < ujung_tengah.y and ujung_kelingking.y < ujung_manis.y):
        return "Metal"    
    
    return "Gesture Tidak Diketahui"

# Fungsi untuk mendeteksi tangan dengan mediapipe
def detect_hand_gesture(image, hand):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hand.process(image_rgb)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Deteksi Gesture
            gesture = recognize_gesture(hand_landmarks)
            # Menggambar tangan terdeteksi pada frame/image
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Menampilkan Teks Gesture
            cv2.putText(image, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    return image

# Membuka kamera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Tidak Dapat Mengakses Kamera")
    exit()

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        print("Gagal Menangkap Frame")
        break
    
    frame = detect_hand_gesture(frame, hands)
    
    # Menampilkan Frame
    cv2.imshow("Hand Gesture Recognition", frame)  

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

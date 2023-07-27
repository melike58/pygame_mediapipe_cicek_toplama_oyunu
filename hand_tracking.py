import cv2
import mediapipe as mp
from settings import *
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands



class HandTracking: #el izleme için oluşturulan sınıftır. 
    def __init__(self): #
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) #el izlemeyi gerçekleştirmek için kullanılacak parameterlerle birlikte el takip nesnesi oluşturuluru.
        self.hand_x = 0
        self.hand_y = 0
        self.results = None #el izleme sonuçlarının saklandığı değişkendir.
        self.hand_closed = False #elin kapalı olup olmadığını belirtir.


    def scan_hands(self, image): #ellerin konumunu belli eder ve bunları görselleştirir.
        rows, cols, _ = image.shape

        
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
       
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)

        image.flags.writeable = True #görüntü üzerindeki verilerin değiştirilebilir olmasını engeller.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        self.hand_closed = False

        if self.results.multi_hand_landmarks: #birden fazla el tespit edilmişse bu blok çalışır 
            for hand_landmarks in self.results.multi_hand_landmarks: #her el için bloğun içindeki işlemler yapılır
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y

                self.hand_x = int(x * SCREEN_WIDTH)
                self.hand_y = int(y * SCREEN_HEIGHT)

                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y

                if y1 > y:
                    self.hand_closed = True

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        return image

    def get_hand_center(self): #elin merkez konumunu gösterir.
        return (self.hand_x, self.hand_y)


    def display_hand(self): #elin gösterildiği pencere opencv kütüphanesiyle yapılırç
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_hand_closed(self):

        pass



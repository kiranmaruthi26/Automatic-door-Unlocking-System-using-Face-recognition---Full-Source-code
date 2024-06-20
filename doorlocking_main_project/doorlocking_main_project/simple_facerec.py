import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        encoded_files_with_ext = glob.glob(os.path.join("./images/encoded_files", "*.*"))
        encoded_files_without_ext = []
        loaded_img_path = []

        for en_img in encoded_files_with_ext:
            encoded_files_without_ext.append(en_img.split("/")[2].split('.')[0][14:])
        for img in images_path:
            loaded_img_path.append(img.split('.')[0][7:])
        #print(encoded_files_without_ext)
        #print(loaded_img_path)

        for img_en_file in encoded_files_without_ext:
            if img_en_file not in loaded_img_path:
                os.remove('./images/encoded_files/'+img_en_file+".txt")
                print(img_en_file+'.txt - Not found in original images - deleted.')
                encoded_files_without_ext.remove(img_en_file)


        print("{} encoding images found.".format(len(images_path) - len(encoded_files_without_ext)))

        # Store image encoding and names
        for img_path in images_path:

            #print(img_path.split('.')[0][7:])
            img_path_splited = img_path.split('.')[0][7:]
            if img_path.split('.')[0][7:] not in encoded_files_without_ext:
                print(img_path)
                print(1)
                img = cv2.imread(img_path)
                print(2)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                print(3)

                # Get the filename only from the initial file path.
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)
                print(4)
                # Get encoding
                img_encoding = face_recognition.face_encodings(rgb_img)[0]


                print(img_encoding)
                print(f"Type : ", type(img_encoding))

                np.savetxt("images/encoded_files/" + filename + ".txt", img_encoding, fmt='%f')
                print(5)

            # Store file name and file encoding

            img_encoding = np.loadtxt("images/encoded_files/" + img_path_splited + ".txt", dtype=float)
            #print(img_encoding)
            #print(type(img_encoding))

            #print(type(img_encoding))
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(img_path_splited)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names

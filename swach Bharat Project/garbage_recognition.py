import cv2
import numpy as np
import imutils


def liquid():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/oil.jpg', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This item qualifies as Liquid waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This is not a Liquid waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def hazardous():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/battery.jpg', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'DANGER: ', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.putText(frame, 'This is a hazardous waste', (50, 83), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This is not a hazardous waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def medical():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/bandage.png', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This is a medical waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This is not a medical waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def ewaste():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/mobile.jpg', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This ia an E-Waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'This is not an E-Waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def recycle():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/bottle.png', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'Item can be recycled', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'Item cannot be recycled', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

def green():
    def ORB_detector(new_image, image_template):
        # Function that compares input image to template
        # It then returns the number of ORB matches between them

        image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

        # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
        orb = cv2.ORB_create(1000, 1.2)

        # Detect keypoints of original image
        kp1, des1 = orb.detectAndCompute(image1, None)

        # Detect keypoints of rotated image
        kp2, des2 = orb.detectAndCompute(image_template, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        # Sort the matches based on distance.  Least distance
        matches = sorted(matches, key=lambda val: val.distance)
        return len(matches)

    cap = cv2.VideoCapture(0)

    # Load our image template, this is our reference image
    image_template = cv2.imread('images/leaf.jpg', 0)

    while True:

        # Get webcam images
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (127, 50, 127), 3)

        # Crop window of observation
        cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        frame = cv2.flip(frame, 1)

        # Get number of ORB matches
        matches = ORB_detector(cropped, image_template)

        # Display current no. of matches
        output_string = "Matches = " + str(matches)
        cv2.putText(frame, output_string, (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 150), 2)

        # Our threshold to indicate object deteciton
        threshold = 20

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'It is Green Waste' , (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        if matches < threshold:
            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame, 'It is not a green waste', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

        cv2.imshow('Garbage Classifier', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
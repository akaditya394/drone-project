# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('best.pt')

# # Open the video file
# video_path = input("Enter the video path: ")
# cap = cv2.VideoCapture(video_path)

# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Display the annotated frame
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('best.pt')

# # Open the video file
# video_path = input("Enter the video path: ")
# cap = cv2.VideoCapture(video_path)

# # Get the video properties
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Change the codec as per your requirement
# out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Write the annotated frame to the output video file
#         out.write(annotated_frame)

#         # Display the annotated frame
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object, close the display window, and release the output video object
# cap.release()
# out.release()
# cv2.destroyAllWindows()



# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('best.pt')

# # Open the image file
# image_path = input("Enter the image path: ")
# image = cv2.imread(image_path)

# # Run YOLOv8 inference on the image
# results = model(image)

# # Visualize the results on the image
# annotated_image = results[0].plot()

# # Save the annotated image to a new file
# output_path = 'annotated_' + image_path
# cv2.imwrite(output_path, annotated_image)

# # Display the annotated image
# cv2.imshow("YOLOv8 Inference", annotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import os.path
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('best.pt')

# Define the input file path
input_path = input("Enter the input file path: ")

# Check if the input is a video or an image
if os.path.isfile(input_path) and input_path.endswith('.mp4'):
    # Open the video file
    cap = cv2.VideoCapture(input_path)

    # Get the video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Change the codec as per your requirement
    output_path = 'annotated_' + input_path
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Write the annotated frame to the output video file
            out.write(annotated_frame)

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object, close the display window, and release the output video object
    cap.release()
    out.release()
    cv2.destroyAllWindows()

elif os.path.isfile(input_path) and (input_path.endswith('.jpg') or input_path.endswith('.jpeg') or input_path.endswith('.png')):
    # Read the image file
    image = cv2.imread(input_path)

    # Run YOLOv8 inference on the image
    results = model(image)

    # Visualize the results on the image
    annotated_image = results[0].plot()

    # Save the annotated image to a new file
    output_path = 'annotated_' + input_path
    cv2.imwrite(output_path, annotated_image)

    # Display the annotated image
    cv2.imshow("YOLOv8 Inference", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('Invalid input file path or file format.')
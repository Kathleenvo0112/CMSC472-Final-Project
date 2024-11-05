import cv2
import os

# Function to extract frames from a video for up to 30 seconds, 1 frame per second
def extract_frames(video_file, duration_limit=30):
    cap = cv2.VideoCapture(video_file)
    
    # Get the video properties
    video_fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = 30
    
    # Limit processing to 30 seconds of video
    max_frames = min(int(video_fps * duration_limit), total_frames)
    
    frame_count = 0
    
    # Get the video file's name without extension
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    
    # Create an output folder with a name corresponding to the video
    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)
    
    while frame_count < max_frames:
        # Move to the correct second in the video (1 frame per second)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count * video_fps)
        
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # Save the frame as an image
        output_file = f"{output_directory}/frame_{frame_count}.jpg"
        cv2.imwrite(output_file, frame)
        print(f"Frame {frame_count} has been extracted and saved as {output_file}")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = r"video1.mov"  # Replace with your video's name
    
    extract_frames(video_file)

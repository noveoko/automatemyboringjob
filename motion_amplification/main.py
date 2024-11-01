import cv2
import numpy as np
from collections import deque

class MotionAmplifier:
    def __init__(self, alpha=16, beta=1, buffer_size=5):
        self.alpha = alpha
        self.beta = beta
        self.buffer_size = buffer_size
        self.frame_buffer = deque(maxlen=buffer_size)

    def process_frame(self, frame):
        """Process a single frame and apply MEMAD."""
        # Split frame into color channels
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(frame)

        # Initialize buffers for each channel
        if len(self.frame_buffer) < self.buffer_size:
            R_buffer = [np.zeros_like(R) for _ in range(self.buffer_size)]
            G_buffer = [np.zeros_like(G) for _ in range(self.buffer_size)]
            B_buffer = [np.zeros_like(B) for _ in range(self.buffer_size)]
        else:
            R_buffer = [img[0] for img in self.frame_buffer]
            G_buffer = [img[1] for img in self.frame_buffer]
            B_buffer = [img[2] for img in self.frame_buffer]

        # Apply MEMAD filter
        R_out = self.beta * R + self.alpha * (R - sum(R_buffer) / len(R_buffer))
        G_out = self.beta * G + self.alpha * (G - sum(G_buffer) / len(G_buffer))
        B_out = self.beta * B + self.alpha * (B - sum(B_buffer) / len(B_buffer))

        # Clip to valid range
        R_out = np.clip(R_out, 0, 255).astype(np.uint8)
        G_out = np.clip(G_out, 0, 255).astype(np.uint8)
        B_out = np.clip(B_out, 0, 255).astype(np.uint8)

        # Merge channels back
        amplified_frame = cv2.merge((R_out, G_out, B_out))
        amplified_frame = cv2.cvtColor(amplified_frame, cv2.COLOR_RGB2BGR)

        # Update frame buffer
        self.frame_buffer.append((R, G, B))
        
        return amplified_frame

    def process_video(self, input_video_path, output_video_path):
        """Process a video and save the amplified output."""
        cap = cv2.VideoCapture(input_video_path)

        # Get video properties
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            amplified_frame = self.process_frame(frame)
            out.write(amplified_frame)

            # Display the frame for debugging (optional)
            cv2.imshow('Amplified Motion', amplified_frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

def main():
    input_path = 'rain_a.mp4'  # example input video
    output_path = 'rain_b_amplified.mp4'  # example output video

    amplifier = MotionAmplifier(alpha=32, beta=1, buffer_size=5)
    amplifier.process_video(input_path, output_path)

if __name__ == "__main__":
    main()

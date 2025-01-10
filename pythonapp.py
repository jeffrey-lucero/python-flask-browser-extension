import os
import shutil
import time
from flask import Flask, request, jsonify
import threading
import logging
from flask_cors import CORS

# Set initial paths
chrome_downloads_dir = os.path.expanduser("~/Downloads")

destination_dir = "C:\\tempdownload"

# Ensure the destination folder exists
os.makedirs(destination_dir, exist_ok=True)

# Configure logging
logging.basicConfig(filename='file_move.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Flask app to handle dynamic directory change
app = Flask(__name__)
CORS(app)

@app.route('/update_directory', methods=['POST'])
def update_directory():
    global destination_dir
    try:
        datas = request.get_json()
        
        new_directory = request.json.get('directory')
        destination_dir  = request.json.get('directory')
        print("Received data:", new_directory)
        if new_directory and os.path.isdir(new_directory):
            # Process the directory update
            return jsonify({'success': True, 'message': new_directory}), 200
        else:
            
            return jsonify({'success': False, 'message': 'Invalid directory'}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'message': 'Error processing the request'}), 500

def move_jpg_files():
    global destination_dir
    while True:
        for filename in os.listdir(chrome_downloads_dir):
            if filename.lower().endswith('.jpeg') or filename.lower().endswith('.aba'):
                
                
                source = os.path.join(chrome_downloads_dir, filename)
                destination = os.path.join(destination_dir, filename)

                # Check if the file already exists in the destination folder
                if os.path.exists(destination):
                    # If file exists, modify the filename by adding an underscore and counter
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    new_filename = f"{base}_{counter}{ext}"
                    destination = os.path.join(destination_dir, new_filename)

                    # Keep incrementing the counter until a unique filename is found
                    while os.path.exists(destination):
                        counter += 1
                        new_filename = f"{base}_{counter}{ext}"
                        destination = os.path.join(destination_dir, new_filename)

                # Log the file move action
                logging.info(f"Moving file: {filename} from {source} to {destination}")

                try:
                    shutil.move(source, destination)
                    print(f"Moved: {filename} -> {destination}")
                    # Log the successful move
                    logging.info(f"Successfully moved: {filename} -> {destination}")
                except Exception as e:
                    print(f"Error moving file: {e}")
                    # Log the error
                    logging.error(f"Error moving {filename}: {e}")

        time.sleep(5)  # Check every 5 seconds

# Start the Flask server in the main thread
def start_flask():
    # Disable the reloader and debugger
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

if __name__ == '__main__':
    # Start Flask server in the main thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True  # Make sure it terminates when the main program exits
    flask_thread.start()

    # Start the file moving process in the background
    move_jpg_files()


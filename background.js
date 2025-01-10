chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'updateDirectory') {
      const newDirectory = message.directory;
      
      // Send the POST request to the Flask server to update the destination directory
      fetch('http://localhost:5000/update_directory', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ directory: newDirectory })
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
            sendResponse({ success: true,message: "New Directory : " + data.message });
        } else {
            sendResponse({ success: false,message: data.message  });
        }
      })
      .catch(error => {
          console.error('Error:', error);
          sendResponse({ success: false,message: data.message  });
      });

      // Return true to indicate you are using async response
      return true;
  }
});

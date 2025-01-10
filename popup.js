document.getElementById('changeBtn').addEventListener('click', function() {
   
    const newDirectory = document.getElementById('directory').value;
    console.log(newDirectory);  // Debugging log
    // Save the new directory to localStorage
    localStorage.setItem('savedDirectory', newDirectory);

    // Send a message to the background script to update the server
    chrome.runtime.sendMessage(
      { action: 'updateDirectory', directory: newDirectory },
      function(response) {
        
        if (response.success) {
          alert(response.message);
        } else {
          alert(response.message);
        }
      }
    );
});

// When the page loads, check localStorage and update the input box if a directory is saved
document.addEventListener('DOMContentLoaded', function() {
    const savedDirectory = localStorage.getItem('savedDirectory');
    if (savedDirectory) {
        document.getElementById('directory').value = savedDirectory;
    }
});




// document.getElementById('changeBtn').addEventListener('click', function() {
//     const newDirectory = document.getElementById('directory').value;
  

//     // Save the new directory to localStorage
//     localStorage.setItem('savedDirectory', newDirectory);

//     // Send a POST request to the Flask server to update the destination directory
//     fetch('http://localhost:5000/update_directory', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ directory: newDirectory })
//     })
//     .then(response => response.json())
//     .then(data => {
//       alert(data.message);
//     })
//     .catch(error => {
//       console.error('Error:', error);
//     });
//   });
  


//   // When the page loads, check localStorage and update the input box if a directory is saved
// document.addEventListener('DOMContentLoaded', function() {
//     const savedDirectory = localStorage.getItem('savedDirectory');
//     if (savedDirectory) {
//         document.getElementById('directory').value = savedDirectory;
//     }
// });
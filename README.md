# Building an LLM Model using Google Gemini API
## Creating a ChatGPT Clone with Gemini and Streamlit

<div align="center">
    <img src="chatbot-output.png" alt="Logo" width="400" height="250">
</div>

<div align="center">
    <img src="imagereader-output.png" alt="Logo" width="400" height="250">
</div>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Side-by-Side Images</title>
  <style>
    /* Add some basic styling to the container */
    .image-container {
      display: table;
      width: 100%;
      border-collapse: collapse;
    }

    /* Style for individual cells (image containers) */
    .image-cell {
      display: table-cell;
      padding: 10px;
      text-align: center;
      border: 1px solid #ddd; /* Add border for separation */
    }

    /* Style for the images */
    .image {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto; /* Center the image in the cell */
    }
  </style>
</head>
<body>

<div class="image-container">
  <div class="image-cell">
    <img src="chatbot-output.png" alt="Image 1" class="image">
    <p>Caption for Image 1</p>
  </div>
  <div class="image-cell">
    <img src="imagereader-output.png" alt="Image 2" class="image">
    <p>Caption for Image 2</p>
  </div>
</div>

</body>
</html>

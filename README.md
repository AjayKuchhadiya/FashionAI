# FashionAI


## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Future Work](#FutureWork)

## Description

FashionAI is an AI-based eCommerce platform that integrates advanced machine learning and AI technologies to enhance the shopping experience. It leverages collaborative filtering, visual search, and generative AI to provide personalized recommendations and innovative search capabilities.

## Features

1. **Visual Search**: Users can upload any fashion-related image, and using ResNet-50, the most similar products will be shown to the user.
2. **Collaborative Filtering**: Items are recommended to users based on the similarity of user profiles (using K-Nearest Neighbors).
3. **Generative AI**: 
   - Text to image generation using an open-source Stable Diffusion model.
   - Large Language Model (LLM) is used to verify if the description provided by the user pertains to a fashion product. If not, no image is generated; if yes, an image is generated.

## Installation

### Prerequisites
- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [React](https://reactjs.org/docs/getting-started.html)

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/AjayKuchhadiya/FashionAI.git
    cd FashionAI/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server:
    ```bash
    flask run
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the required packages:
    ```bash
    npm install
    ```

3. Start the React application:
    ```bash
    npm run dev
    ```

## Usage

1. Upload a fashion-related image to utilize the visual search feature and receive similar product recommendations.
2. Get personalized recommendations based on collaborative filtering by interacting with the platform.
3. Generate images from text descriptions related to fashion using the generative AI feature.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## Future Work:
1. Adding a chatbot
2. Text to text search (we trained a model for the same but due to low accuracy we had to drop it)
---

Feel free to modify and expand this template as needed to better fit your project's specifics.

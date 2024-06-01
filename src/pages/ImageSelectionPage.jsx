import { useState, useEffect } from 'react';
import axios from 'axios';
import { useUser } from '../UserContext';
import './ImageSelectionPage.css'; // Import the CSS file

export default function ImageSelectionPage({ onSelectionComplete }) {
  const { setHasSelectedImages } = useUser();
  const [selectedImages, setSelectedImages] = useState([]);
  const [images, setImages] = useState([]);
  const [recommendedImages, setRecommendedImages] = useState([]);

  useEffect(() => {
    async function fetchImages() {
      try {
        const response = await axios.get('/api/images');
        setImages(response.data);
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    }

    fetchImages();
  }, []);

  const handleImageClick = (image) => {
    setSelectedImages(prev => {
      if (prev.includes(image)) {
        return prev.filter(img => img !== image);
      } else {
        return [...prev, image];
      }
    });
  };

  const handleContinue = async () => {
    if (selectedImages.length >= 5) {
      try {
        const response = await axios.post('/api/selected-images', { selected_images: selectedImages });
        setRecommendedImages(response.data);
        setHasSelectedImages(true);
        onSelectionComplete();
      } catch (error) {
        console.error('Error submitting selected images:', error);
      }
    } else {
      alert('Please select at least 5 images');
    }
  };

  return (
    <div>
      <h1>Select at least 5 images</h1>
      <div className="image-grid">
        {images.map((image, index) => (
          <img
            key={index}
            src={`/api/uploads/${image}`}
            alt={image}
            onClick={() => handleImageClick(image)}
            className={selectedImages.includes(image) ? 'selected' : ''}
          />
        ))}
      </div>
      <button onClick={handleContinue}>Continue</button>
      {recommendedImages.length > 0 && (
        <div>
          <h2>Recommended Images</h2>
          <div className="image-grid">
            {recommendedImages.map((image, index) => (
              <img
                key={index}
                src={`/api/uploads/${image}`}
                alt={image}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

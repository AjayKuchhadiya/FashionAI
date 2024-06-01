import { useState, useEffect } from 'react';
import axios from 'axios';
import { useUser } from '../UserContext';

export default function ImageSelectionPage({ onSelectionComplete }) {
  const { setHasSelectedImages } = useUser();
  const [selectedImages, setSelectedImages] = useState([]);
  const [images, setImages] = useState([]);

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

  const handleContinue = () => {
    if (selectedImages.length >= 5) {
      setHasSelectedImages(true);
      onSelectionComplete();
    } else {
      alert('Please select at least 5 images');
    }
  };

  return (
    <div>
      <h1>Select at least 5 images</h1>
      <div className="image-grid">
        {images.map(image => (
          <img
            key={image}
            src={`path/to/your/images/${image}`}  // Adjust the path to where your images are stored
            alt={image}
            onClick={() => handleImageClick(image)}
            style={{ border: selectedImages.includes(image) ? '2px solid blue' : 'none' }}
          />
        ))}
      </div>
      <button onClick={handleContinue}>Continue</button>
    </div>
  );
}

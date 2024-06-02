import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useUser } from '../UserContext';
import ImageSelectionPage from './ImageSelectionPage';

export default function IndexPage() {
  const { user, hasSelectedImages } = useUser();
  const [recommendedImages, setRecommendedImages] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [uploadedProducts, setUploadedProducts] = useState([]);

  const handleImageUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    setUploading(true);
    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setUploadedProducts(response.data);
    } catch (error) {
      console.error('Error uploading image:', error);
    } finally {
      setUploading(false);
    }
  };

  const handleSelectionComplete = (images) => {
    setRecommendedImages(images);
  };

  useEffect(() => {
    if (hasSelectedImages && recommendedImages.length === 0) {
      // Fetch the recommended images again if needed
      // This part depends on your application logic
    }
  }, [hasSelectedImages]);

  if (!user) {
    return (
      <div>
        Please Login First
      </div>
    );
  }

  if (!hasSelectedImages) {
    return <ImageSelectionPage onSelectionComplete={handleSelectionComplete} />;
  }

  return (
    <div>
      <div style={styles.uploadSection}>
        <h2>Upload an Image</h2>
        <input type="file" onChange={handleImageUpload} />
        {uploading && <p>Uploading...</p>}
      </div>
      <div style={styles.recommendedSection}>
        <h2>Recommended Products</h2>
        <div style={styles.productGrid}>
          {recommendedImages.map((product, index) => (
            <div key={index} style={styles.productItem}>
              <img src={`api/uploads/${product.image_path.split('/').pop()}`} alt={product.product_name} style={styles.productImage} />
              <p>{product.product_name}</p>
            </div>
          ))}
        </div>
      </div>
      <div style={styles.uploadedProductsSection}>
        {uploadedProducts.length > 0 && (
          <>
            <h2>Uploaded Products</h2>
            <div style={styles.productGrid}>
              {uploadedProducts.map(product => (
                <div key={product.id} style={styles.productItem}>
                  <img src={product.image_url} alt={product.name} style={styles.productImage} />
                  <p>{product.name}</p>
                  <p>${product.price}</p>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  uploadSection: {
    margin: '20px 0',
  },
  recommendedSection: {
    margin: '20px 0',
  },
  uploadedProductsSection: {
    margin: '20px 0',
  },
  productGrid: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  productItem: {
    flexBasis: 'calc(20% - 10px)', // 5 items per row with some spacing
    margin: '5px',
    boxSizing: 'border-box',
  },
  productImage: {
    width: '50%', // Reduce size to 50%
    height: 'auto',
  },
};

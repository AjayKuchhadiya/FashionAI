import { useState } from 'react';
import axios from 'axios';
import { useUser } from '../UserContext';

export default function IndexPage() {
  const { user, hasSelectedImages } = useUser();
  const [products, setProducts] = useState([]);
  const [uploading, setUploading] = useState(false);

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
      setProducts(response.data);
    } catch (error) {
      console.error('Error uploading image:', error);
    } finally {
      setUploading(false);
    }
  };

  if (!user) {
    return (
      <div>
        Please Login First
      </div>
    );
  }

  if (!hasSelectedImages) {
    return (
      <div>
        Please select at least 5 images first.
      </div>
    );
  }

  return (
    <div>
      <input type="file" onChange={handleImageUpload} />
      {uploading && <p>Uploading...</p>}
      <div className="product-grid">
        {products.map(product => (
          <div key={product.id} className="product-item">
            <img src={product.image_url} alt={product.name} />
            <p>{product.name}</p>
            <p>${product.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

import { Routes, Route } from 'react-router-dom'
import './App.css'
import IndexPage from './pages/IndexPage'
import LoginPage from './pages/LoginPage'
import Layout from './Layout'
import RegisterPage from './pages/RegisterPage'
import ImageSelectionPage from './pages/ImageSelectionPage'

function App() {

  const handleSelectionComplete = () => {
    // Perform any necessary actions like saving user preferences
    // For now, we'll just redirect to the home page (shopping page)
    window.location.href = '/'; // Redirect to the shopping page
  };

  
  return (
    <Routes>
      <Route path="/" element={<Layout/>}>
        <Route index element={<IndexPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/select-images" element={<ImageSelectionPage onSelectionComplete={handleSelectionComplete} />} />
      </Route>
    </Routes>
  )
}

export default App

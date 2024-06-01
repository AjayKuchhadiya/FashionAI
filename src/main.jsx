import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter } from 'react-router-dom'
import { UserContextProvider } from './UserContext.jsx' // Import UserContextProvider

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <UserContextProvider> {/* Wrap App with UserContextProvider */}
        <App />
      </UserContextProvider>
    </BrowserRouter>
  </React.StrictMode>,
)

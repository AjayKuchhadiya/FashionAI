import { Link } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

export default function RegisterPage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  async function registerUser(ev) {
    ev.preventDefault();
    try {
      const response = await axios.post('/api/register', {  // Updated to use /api prefix
        name,
        email,
        password,
      });
      console.log(response.data);  // Logging response from backend (optional)
      alert('Registration successful. Now you can log in');
      // Optionally, redirect the user to the login page after successful registration
      // history.push('/login');
    } catch (e) {
      console.error(e);  // Logging error (optional)
      if (e.response && e.response.data && e.response.data.error) {
        setError(e.response.data.error);
      } else {
        setError('Registration failed. Please try again later');
      }
    }
  }

  return (
    <div className="mt-4 grow flex items-center justify-around">
      <div className="mt-60">
        <h1 className="text-4xl text-center mb-4">Register</h1>
        {error && <div className="text-red-500 mb-4">{error}</div>}
        <form className="max-w-md mx-auto" onSubmit={registerUser}>
          <input type="text"
                 placeholder="John Doe"
                 value={name}
                 onChange={ev => setName(ev.target.value)} />
          <input type="email"
                 placeholder="your@email.com"
                 value={email}
                 onChange={ev => setEmail(ev.target.value)} />
          <input type="password"
                 placeholder="password"
                 value={password}
                 onChange={ev => setPassword(ev.target.value)} />
          <button className="primary">Register</button>
          <div className="text-center py-2 text-gray-500">
            Already a member? <Link className="underline text-black" to={'/login'}>Login</Link>
          </div>
        </form>
      </div>
    </div>
  );
}
import { Link, Navigate } from "react-router-dom";
import { useContext, useState } from "react";
import axios from "axios";
import { UserContext } from "../UserContext.jsx"; // Adjust the path if necessary

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [redirect, setRedirect] = useState(false);
  const { setUser } = useContext(UserContext); // Destructure setUser from UserContext
  const [error, setError] = useState('');

  async function handleLoginSubmit(ev) {
    ev.preventDefault();
    try {
      const { data } = await axios.post('/api/login', { email, password });
      setUser(data.user);  // Correctly setting the user data
      alert('Login successful');
      setRedirect(true);
    } catch (e) {
      console.error(e);  // Logging error for debugging
      if (e.response && e.response.data && e.response.data.error) {
        setError(e.response.data.error);
      } else {
        setError('Login failed. Please try again later');
      }
    }
  }

  if (redirect) {
    return <Navigate to={'/select-images'} />;
  }

  return (
    <div className="mt-4 grow flex items-center justify-around">
      <div className="mt-60">
        <h1 className="text-4xl text-center mb-4">Login</h1>
        {error && <div className="text-red-500 mb-4">{error}</div>}
        <form className="max-w-md mx-auto" onSubmit={handleLoginSubmit}>
          <input
            type="email"
            placeholder="your@email.com"
            value={email}
            onChange={ev => setEmail(ev.target.value)}
          />
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={ev => setPassword(ev.target.value)}
          />
          <button className="primary">Login</button>
          <div className="text-center py-2 text-gray-500">
            Don't have an account yet? <Link className="underline text-black" to={'/register'}>Register now</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

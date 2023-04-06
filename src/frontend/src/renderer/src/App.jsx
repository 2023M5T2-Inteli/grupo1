/* Este é um app em React. A relação de páginas (Router) se encontra neste script, utilizando scripts de 
outros páginas da pasta "pages". 
*/

// Importa recursos necessários
import { Routes, Route, HashRouter as Router } from 'react-router-dom'; // Importa recursos de rotas

// Páginas
import History from './pages/History';
import Home from './pages/Home';
import Profile from './pages/Profile';

// Componente principal
function App() {


  return (
    <div>
      <Router> {/* Define o roteador */}
        <Routes>

          <Route path='/' element={<Home />} /> {/* Define a rota inicial */}
          <Route path='/archive' element={<History />} /> {/* Define a rota para a página de histórico */}
          <Route path='/profile' element={<Profile/>} /> {/* Define a rota para a página de perfil (em construção) */}
        </Routes>
      </Router>

    </div>
  );
}

export default App;

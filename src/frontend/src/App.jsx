/* Este é um app em React. A relação de páginas (Router) se encontra neste script, utilizando scripts de 
outros páginas da pasta "pages". 
*/

// Importa recursos necessários
import { Routes, Route, BrowserRouter as Router, BrowserRouter } from 'react-router-dom'; // Importa recursos de rotas

// Páginas
import History from './pages/History';
import Demo from './pages/Demo';
import Home from './pages/Home';
import Sidebar from './components/Sidebar';

// Componente principal
function App() {
  return (
    <div>
      <BrowserRouter> {/* Define o roteador */}
        <Routes> 
          <Route path='/' element={<Home />} /> {/* Define a rota inicial */}
          <Route path='/demo' element={<Demo />} /> {/* Define a rota para a página de demonstração */}
          <Route path='/archive' element={<History />} /> {/* Define a rota para a página de histórico */}
          <Route path='/profile' element={<div>
            <Sidebar /><h1 className='ml-20'>Em construção</h1></div>} /> {/* Define a rota para a página de perfil (em construção) */}
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;

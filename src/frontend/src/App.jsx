/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários
import { Routes, Route, BrowserRouter as Router, BrowserRouter } from 'react-router-dom';
import History from './pages/History';
import Demo from './pages/Demo';
import Home from './pages/Home';
import Sidebar from './components/Sidebar';

// Componente principal
function App() {
  // Elementos a serem mostrados na tela
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/demo' element={<Demo />} />
          <Route path='/archive' element={<History />} />
          <Route path='/profile' element={<div>
            <Sidebar /><h1 className='ml-20'>Em construção</h1></div>} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;

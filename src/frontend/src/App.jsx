/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários
import { Routes, Route, BrowserRouter as Router, BrowserRouter } from 'react-router-dom';
import History from './pages/History';
import Begin from './pages/Begin';
import Home from './pages/Home';
import Ancient from './pages/ancient';

// Componente principal
function App() {
  // Elementos a serem mostrados na tela
  return (
    <div>
      <BrowserRouter>
      <Routes>
            <Route path='/' element={<Begin />} />
            <Route path='/home' element={<Home />}/>
            <Route path='/archive' element={<History />}/>
            <Route path='/ancient' element={< Ancient/>}/>
      </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;

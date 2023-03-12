/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários
import { Routes, Route, BrowserRouter as Router, BrowserRouter } from 'react-router-dom';
import History from './pages/History';
import Begin from './pages/Begin';

// Componente principal
function App() {
  // Elementos a serem mostrados na tela
  return (
    <div>
      <BrowserRouter>
      <Routes>
            <Route path='/' element={<Begin />} />
            <Route path='/history' element={<History />}/>
      </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;

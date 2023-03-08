/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários
import { useState, useEffect } from "react"; // Hook para controlar estado dos componentes
import Axios from "axios"; // Biblioteca para fazer requisições HTTP
import bgWaves from "./assets/bg-waves.png"; // Vetor de decoração na base da página
import Button from "./components/Button";
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
            <Route path='/teste' element={<Begin />} />
            <Route path='/history' element={<History />}/>
      </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;

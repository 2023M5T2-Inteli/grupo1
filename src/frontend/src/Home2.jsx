import Sidebar from './components/Sidebar'
import StartButton from './assets/startButton.jpeg'

// Componente principal
function App() {
    return (
    <div className='min-height-full h-full'>
            <aside className='sidebar bg-blue-900 text-center'>
                <h3>Tectonics</h3>
                <nav>
                    <div>
                        <a>Home</a>
                    </div>
                    <div>
                        <a>Histórico</a>
                    </div>
                </nav>
            </aside>

            <main>
                <h1>Welcome</h1>
                <a>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro, nesciunt obcaecati sunt ratione, sint odit magnam aliquam veritatis recusandae error earum omnis ullam, totam aperiam quo nemo velit repellendus. Impedit.</a>
            </main>
    </div>
    )
}

export default App

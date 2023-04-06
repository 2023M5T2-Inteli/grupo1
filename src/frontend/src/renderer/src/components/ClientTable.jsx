import { useState, useEffect } from 'react';

export function ClientTable() {
    const [data, setData] = useState([]);
    const [selectedItem, setSelectedItem] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [showAddModal, setShowAddModal] = useState(false);
    const [newCnpj, setNewCnpj] = useState('');
    const [newName, setNewName] = useState('');
    const [projectName, setProjectName] = useState('');

    const handleAddClient = () => {
        fetch('http://127.0.0.1:5000/client', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                full_name: newName,
                cnpj: newCnpj
            })
        }).then(() => {
            setShowAddModal(false);
            setNewName('');
            setNewCnpj('');
            fetchData(); // refetch data after adding user
        })
            .catch((error) => console.log(error));
    };

    const fetchData = () => {
        fetch('http://127.0.0.1:5000/client')
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.log(error));
    };

    useEffect(() => {
        fetchData();
    }, []);

    const handleRowClick = (item) => {
        setSelectedItem(item);
        setShowModal(true);
    };

    const handleModalClose = () => {
        setSelectedItem(null);
        setShowModal(false);
    };

    const handleAddModalClose = () => {
        setShowAddModal(false);
    };

    return (
        <div>
            <h3>Clientes</h3>
            <div>
                <table className="border-collapse table-fixed">
                    <thead>
                        <tr>
                            <th className="w-1/2 py-2 px-4 border-b-2 border-gray-500 font-bold uppercase text-sm text-left">
                                Nome
                            </th>
                            <th className="w-1/2 py-2 px-4 border-b-2 border-gray-500 font-bold uppercase text-sm text-left">
                                CNPJ
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {console.log({ data })}
                        {data.map((item) => (
                            <tr
                                key={item.id}
                                className="hover:bg-gray-100 cursor-pointer"
                                onClick={() => handleRowClick(item)}
                            >
                                <td className="w-1/2 py-2 px-4 border-b border-gray-500 text-sm">{item.full_name}</td>
                                <td className="w-1/2 py-2 px-4 border-b border-gray-500 text-sm">{item.cnpj}</td>

                            </tr>
                        ))}
                    </tbody>
                </table>
                <div className="flex justify-end mt-4">
                    <button
                        className="bg-purple hover:bg-[#7456ea] text-white font-bold py-2 px-4 rounded"
                        onClick={() => setShowAddModal(true)}
                    >
                        Adicionar
                    </button>
                </div>

                {
                    showModal && (
                        <div className="fixed z-10 inset-0 overflow-y-auto">
                            <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                                <div className="fixed inset-0 transition-opacity">
                                    <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
                                </div>
                                <span className="hidden sm:inline-block sm:align-middle sm:h-screen"></span>&#8203;
                                <div
                                    className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
                                    role="dialog"
                                    aria-modal="true"
                                    aria-labelledby="modal-headline"
                                >
                                    <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                                        <h3 className="text-lg font-medium leading-6 text-gray-900" id="modal-headline">
                                            Projetos para {selectedItem?.full_name}
                                        </h3>
                                        <table className="w-full border-collapse table-fixed mt-4">
                                            <tbody>
                                                {selectedItem.projects.map((project) => (
                                                    <tr key={project.name} >
                                                        <td className="w-1/2 py-2 px-4 border-b border-gray-500 text-sm">{project.name}</td>
                                                    </tr>
                                                ))}
                                                <div className="flex w-full">
                                                    <input
                                                        type="text"
                                                        placeholder="Nome do projeto"
                                                        className="border px-4 py-2 w-1/2 mr-2"
                                                        value={projectName}
                                                        onChange={(e) => setProjectName(e.target.value)}
                                                    />
                                                    <button
                                        type="button"
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-purple hover:bg-[#7456ea] text-base font-medium text-white  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        onClick={handleAddClient}
                                    >
                                        Salvar
                                    </button>

                                                </div>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div className="bg-gray-50 px-4 py-3 flex justify-end">
                                    <button
                                        type="button"
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-gray-500 hover:bg-gray-400 text-base font-medium text-white  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        onClick={handleAddModalClose}
                                    >
                                        Fechar
                                    </button>

                                    <button
                                        type="button"
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-purple hover:bg-[#7456ea] text-base font-medium text-white  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        onClick={handleAddClient}
                                    >
                                        Salvar
                                    </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                }
                {showAddModal && (
                    <div className="fixed z-10 inset-0 overflow-y-auto">
                        <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                            <div className="fixed inset-0 transition-opacity">
                                <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
                            </div>
                            <span className="hidden sm:inline-block sm:align-middle sm:h-screen"></span>&#8203;
                            <div
                                className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
                                role="dialog"
                                aria-modal="true"
                                aria-labelledby="modal-headline"
                            >
                                <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4 mb-4">
                                    <h3 className="text-lg font-medium leading-6 text-gray-900 mb-6" id="modal-headline">
                                        Adicionar novo cliente
                                    </h3>
                                    <div className="flex w-full">
                                        <input
                                            type="text"
                                            placeholder="Nome"
                                            className="border px-4 py-2 w-1/2 mr-2"
                                            value={newName}
                                            onChange={(e) => setNewName(e.target.value)}
                                        />
                                        <input
                                            type="text"
                                            placeholder="CNPJ"
                                            className="border px-4 py-2 w-1/2 mr-2"
                                            value={newCnpj}
                                            onChange={(e) => setNewCnpj(e.target.value)}
                                        />

                                    </div>

                                </div>
                                <div className="bg-gray-50 px-4 py-3 flex justify-end">

                                    <button
                                        type="button"
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-gray-500 hover:bg-gray-400 text-base font-medium text-white  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        onClick={handleAddModalClose}
                                    >
                                        Fechar
                                    </button>

                                    <button
                                        type="button"
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-purple hover:bg-[#7456ea] text-base font-medium text-white  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                                        onClick={handleAddClient}
                                    >
                                        Salvar
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div >
    )
}
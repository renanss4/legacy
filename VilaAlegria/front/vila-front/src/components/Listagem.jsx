import React from "react";

const Listagem = (props) => {
    const { Moradores, editar, excluir } = props;

    return (
        <>
            {Moradores && Moradores.length > 0 &&
                <div className="listagem">
                    <table>
                        <thead>
                            <tr>
                                <th>Nome</th>
                                <th>Email</th>
                                <th>CPF</th>
                                <th>Data de Nascimento</th>
                                <th>Telefone</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Moradores.map(morador => (
                                <tr key={morador.id}>
                                    <td>{morador.nome}</td>
                                    <td>{morador.email}</td>
                                    <td>{morador.cpf}</td>
                                    <td>{morador.dataNascimento}</td>
                                    <td>{morador.telefone}</td>
                                    <td><button onClick={() => editar(morador)}>Editar</button></td>
                                    <td><button onClick={() => excluir(morador.id)}>Excluir</button></td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            }
        </>
    )
}

export default Listagem;
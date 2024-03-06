import React, { useState, useEffect } from "react";
import MoradorService from "../services/MoradorService";

const Cadastro = (props) => {
    const {MoradorAtual, carregarMoradores} = props;

    const [Morador, setMorador] = useState({nome: '', cpf: '', email: '', dataNascimento: '', telefone: 0})

    useEffect(() => {
        setMorador(MoradorAtual)
    }, [MoradorAtual])

    const ProcessMudancas = (event) => {
        const {name, value} = event.target
        setMorador({...Morador, [name]:value })
    }

    const salvarMorador = () => {
        if(!Morador.id) {
            MoradorService.salvarMorador(Morador)
            carregarMoradores()
            return
        } 
        MoradorService.atualizarMorador(Morador)
        carregarMoradores()
    }

    return (
        <>
            <h1>Cadastro</h1>
            <input type="text" name="nome" value={Morador.nome} onChange={ProcessMudancas} />
            <input type="text" name="cpf" value={Morador.cpf} onChange={ProcessMudancas} />
            <input type="text" name="email" value={Morador.email} onChange={ProcessMudancas} />
            <input type="text" name="dataNascimento" value={Morador.dataNascimento} onChange={ProcessMudancas} />
            <input type="number" name="telefone" value={Morador.telefone} onChange={ProcessMudancas} />
            <button onClick={salvarMorador} >Salvar</button>
        </>
    )
}

export default Cadastro;
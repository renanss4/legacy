import React, { useEffect, useState } from "react";
import Listagem from './Listagem'
import Cadastro from "./Cadastro";
import MoradorService from "../services/MoradorService";

const Morador = () => {
    const[Moradores, setMoradores] = useState();
    const[MoradorEdicao, atualizarMoradorEdicao] = useState({nome: ''});

    useEffect(() => {
        carregarMoradores();
    }, [])

    const carregarMoradores = async () => {
        const Moradores = await MoradorService.buscarMoradores();
        setMoradores(Moradores)
    }

    useEffect(() => {
        atualizarMoradorEdicao({id: 1});
    }, [Moradores])

    useEffect(() => {
        // 
    },[MoradorEdicao])

    const editarMorador = Moradores => {
        atualizarMoradorEdicao(Moradores);
    }

    const excluirMorador = async (MoradorId) => {
        await MoradorService.excluirMorador(MoradorId)
        carregarMoradores()
    }

    return (
        <div>
            <Cadastro MoradorAtual = {MoradorEdicao} carregarMoradores = {carregarMoradores}/>
            <Listagem 
                Moradores = {Moradores}
                editar = {editarMorador}
                excluir = {excluirMorador}
            />
        </div>
    )
}

export default Morador
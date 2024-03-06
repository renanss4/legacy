import axios from 'axios';

const BASE_URL = `http://localhost:8080/morador`

class MoradorService {
    buscarMoradores(){
        return axios.get(BASE_URL).then(response => response.data)
    }

    salvarMorador(morador){
        return axios.post(`${BASE_URL}`, morador)
    }

    atualizarMorador(morador) {
        return axios.put(`${BASE_URL}/${morador.id}`, morador)
    }

    excluirMorador(id) {
        return axios.delete(`${BASE_URL}/${id}`)
            .catch(erro => {
                throw erro;
            })
    }
}

export default new MoradorService();
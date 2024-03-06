package com.vila.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.vila.morador.Morador;
import com.vila.repository.MoradorRepository;

@Service
public class MoradorService {

	private final MoradorRepository moradorRepository;
	
	@Autowired
	public MoradorService(MoradorRepository moradorRepository) {
		super();
		this.moradorRepository = moradorRepository;
	}
	
	//GET
	public List<Morador> pegarMoradores() {
		return moradorRepository.findAll();
	}
	
	// GET
	public Morador pegarMoradorPorId(Integer id) {
		return moradorRepository.findMoradorById(id);
	}
	
	// POST
	public void adicionarNovoMorador(Morador morador) {
		Optional<Morador> moradorOptional = moradorRepository.findMoradorByNome(morador.getNome());
			
		if (moradorOptional.isPresent()) {
			throw new IllegalStateException("Nome já cadastrado");
		}
			
		moradorRepository.save(morador);
	}

	// DELETE
	public void excluirMorador(Integer id) {
		boolean existente = moradorRepository.existsById(id);
		if (!existente) {
			throw new IllegalStateException("Morador com id " + id + "não existe.");
		}
		moradorRepository.deleteById(id);
	}
	
	// UPDATE
	public void editarMorador(Morador morador) {
		moradorRepository.save(morador);
	}
}

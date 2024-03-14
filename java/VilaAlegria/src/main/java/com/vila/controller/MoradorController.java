package com.vila.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.vila.morador.Morador;
import com.vila.service.MoradorService;

@RestController
@RequestMapping(path = "/morador")
public class MoradorController {
	
	private MoradorService moradorService;
	
	@Autowired
	public MoradorController(MoradorService moradorService) {
		super();
		this.moradorService = moradorService;
	}
	
	@GetMapping
	public List<Morador> pegarMoradores() {
		return moradorService.pegarMoradores();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Morador> pegarMoradorPorId(@PathVariable Integer id) {
		return new ResponseEntity<>(moradorService.pegarMoradorPorId(id), HttpStatus.OK);
	}
	
	@PostMapping
	@ResponseStatus(HttpStatus.CREATED)
	public void registrarMorador(@RequestBody Morador morador) {
		moradorService.adicionarNovoMorador(morador);
	}
	
	@DeleteMapping("/{id}")
	public void excluirMorador(@PathVariable("id") Integer id) {
		moradorService.excluirMorador(id);
	}
	
	@PutMapping("/{id}")
	public void editarMorador(@RequestBody Morador morador) {
		moradorService.editarMorador(morador);
	}
	
}
